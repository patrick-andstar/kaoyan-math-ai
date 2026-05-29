"use strict";

const {
  Component,
  MarkdownRenderer,
  Modal,
  Notice,
  Plugin,
  Setting,
  TFile,
} = require("obsidian");
const electron = require("electron");
const fs = require("fs");
const path = require("path");

const PLUGIN_ID = "native-single-pdf-export";

function isAbsolutePath(value) {
  return typeof value === "string" && path.isAbsolute(value.trim());
}

function ensurePdfPath(value) {
  const outputPath = (value || "").trim();
  if (!outputPath) {
    throw new Error("Output path is required.");
  }
  if (!isAbsolutePath(outputPath)) {
    throw new Error("Output path must be an absolute path.");
  }
  if (path.extname(outputPath).toLowerCase() !== ".pdf") {
    throw new Error("Output path must end with .pdf.");
  }
  return outputPath;
}

function parseBool(value) {
  return value === true || value === "true" || value === "1";
}

function getPdfSettings(app, outputPath) {
  const config = app.vault.getConfig("pdfExportSettings") || {};
  const margin = config.margin ?? "0";
  const options = {
    includeName: config.includeName ?? true,
    pageSize: config.pageSize || "A4",
    landscape: config.landscape ?? false,
    marginsType: Number.parseInt(margin, 10),
    scaleFactor: config.downscalePercent ?? 100,
    filepath: outputPath,
    open: false,
  };
  if (options.marginsType === 1 || options.marginsType === 2) {
    options.margins = { top: 0, left: 0, bottom: 0, right: 0 };
  }
  options.scale = Math.min(Math.max(options.scaleFactor / 100, 0.1), 2);
  return options;
}

async function renderMarkdown(app, file, container, component, includeName) {
  const preview = container.createDiv("markdown-preview-view markdown-rendered");
  preview.toggleClass("rtl", app.vault.getConfig("rightToLeft"));
  preview.toggleClass("show-properties", app.vault.getConfig("propertiesInDocument") !== "hidden");
  if (includeName) {
    preview.createEl("h1", { text: file.basename });
  }
  const markdown = await app.vault.cachedRead(file);
  if (typeof MarkdownRenderer.render === "function") {
    await MarkdownRenderer.render(app, markdown, preview, file.path, component);
  } else {
    await MarkdownRenderer.renderMarkdown(markdown, preview, file.path, component);
  }
  const links = preview.findAll("a.internal-link");
  for (const link of links) {
    link.removeAttribute("href");
  }
  return preview;
}

function printToPdf(options) {
  return new Promise((resolve, reject) => {
    const ipc = electron.ipcRenderer;
    let timeoutId = null;
    const done = (_event, result) => {
      window.clearTimeout(timeoutId);
      resolve(result);
    };
    timeoutId = window.setTimeout(() => {
      ipc.removeListener("print-to-pdf", done);
      reject(new Error("Timed out waiting for print-to-pdf."));
    }, 60000);
    ipc.once("print-to-pdf", done);
    ipc.send("print-to-pdf", options);
  });
}

function delay(ms) {
  return new Promise((resolve) => window.setTimeout(resolve, ms));
}

async function openMarkdownFile(app, file) {
  const leaf = app.workspace.getLeaf(false);
  await leaf.openFile(file, { active: true });
  await app.workspace.setActiveLeaf(leaf, { focus: true });
  return leaf;
}

class ExportPathModal extends Modal {
  constructor(app, plugin, file) {
    super(app);
    this.plugin = plugin;
    this.file = file;
    this.outputPath = "";
  }

  onOpen() {
    const { contentEl } = this;
    contentEl.empty();
    contentEl.createEl("h2", { text: "Native PDF Export" });
    contentEl.createEl("p", {
      text: `Export ${this.file.path} to an absolute PDF path.`,
      cls: "setting-item-description",
    });
    new Setting(contentEl)
      .setName("Output PDF path")
      .setDesc("Use an absolute path ending in .pdf. Existing files are overwritten.")
      .addText((text) => {
        text.inputEl.style.width = "100%";
        text.setPlaceholder("C:\\Users\\11832\\Desktop\\math-notes\\note.pdf");
        text.onChange((value) => {
          this.outputPath = value;
        });
      });
    new Setting(contentEl).addButton((button) => {
      button
        .setButtonText("Export")
        .setCta()
        .onClick(async () => {
          try {
            await this.plugin.exportFileToPdf(this.file, this.outputPath, { open: false });
            this.close();
          } catch (error) {
            new Notice(`PDF export failed: ${error.message}`);
          }
        });
    });
  }

  onClose() {
    this.contentEl.empty();
  }
}

module.exports = class NativeSinglePdfExportPlugin extends Plugin {
  async onload() {
    this.addCommand({
      id: "export-active-markdown-to-absolute-path",
      name: "Export active Markdown to absolute path",
      checkCallback: (checking) => {
        const file = this.app.workspace.getActiveFile();
        if (!(file instanceof TFile) || file.extension !== "md") {
          return false;
        }
        if (!checking) {
          new ExportPathModal(this.app, this, file).open();
        }
        return true;
      },
    });

    this.registerObsidianProtocolHandler(PLUGIN_ID, async (params) => {
      try {
        await this.handleUriExport(params || {});
      } catch (error) {
        console.error(error);
        new Notice(`PDF export failed: ${error.message}`);
      }
    });
  }

  async handleUriExport(params) {
    const filePath = decodeURIComponent(params.file || "").trim();
    const outputPath = decodeURIComponent(params.output || "").trim();
    const openAfterExport = parseBool(params.open);
    if (!filePath) {
      throw new Error("URI parameter 'file' is required.");
    }
    const abstractFile = this.app.vault.getAbstractFileByPath(filePath);
    if (!(abstractFile instanceof TFile) || abstractFile.extension !== "md") {
      throw new Error(`Markdown file not found: ${filePath}`);
    }
    await openMarkdownFile(this.app, abstractFile);
    await this.exportFileToPdf(abstractFile, outputPath, { open: openAfterExport });
  }

  async exportFileToPdf(file, outputPath, options = {}) {
    if (!(file instanceof TFile) || file.extension !== "md") {
      throw new Error("Source file must be a Markdown file.");
    }
    const pdfPath = ensurePdfPath(outputPath);
    fs.mkdirSync(path.dirname(pdfPath), { recursive: true });

    const body = activeDocument.body;
    const previousClassName = body.className;
    body.addClass("theme-light");
    body.removeClass("theme-dark");

    const printContainer = body.createDiv("print");
    const component = new Component();
    this.addChild(component);
    component.load();
    const cleanup = () => {
      printContainer.detach();
      component.unload();
      body.className = previousClassName;
    };

    try {
      const pdfOptions = getPdfSettings(this.app, pdfPath);
      pdfOptions.open = Boolean(options.open);
      await renderMarkdown(this.app, file, printContainer, component, pdfOptions.includeName);
      await delay(200);
      await printToPdf(pdfOptions);
      new Notice(`PDF saved to ${pdfPath}`);
      if (options.open) {
        await electron.shell.openPath(pdfPath);
      }
    } finally {
      cleanup();
    }
  }
};
