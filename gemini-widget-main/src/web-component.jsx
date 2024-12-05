/* eslint-disable react/no-is-mounted */
import React from "react";
import { createRoot } from "react-dom/client";
import Chatbot from "./components/Chatbot";

class GeminiChatWidget extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
  }

  connectedCallback() {
    const apiKey = this.getAttribute("api-key") || "";
    const model = this.getAttribute("model") || "gemini-1.5-flash";

    const container = document.createElement("div");

    if (this.shadowRoot) {
      this.shadowRoot.appendChild(container);

      const styleSheet = document.createElement("style");
      styleSheet.textContent = `
        @import url('https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css');
        :host { display: block; }
      `;
      this.shadowRoot.appendChild(styleSheet);

      const root = createRoot(container);
      root.render(
        <React.StrictMode>
          <Chatbot apiKey={apiKey} model={model} />
        </React.StrictMode>
      );
    }
  }

  disconnectedCallback() {
    if (this.shadowRoot) {
      const root = this.shadowRoot.querySelector("div");
      if (root) {
        createRoot(root).unmount();
      }
    }
  }
}

if (!customElements.get("gemini-chat-widget")) {
  customElements.define("gemini-chat-widget", GeminiChatWidget);
}

export default GeminiChatWidget;
