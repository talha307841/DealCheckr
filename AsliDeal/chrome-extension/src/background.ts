// This file contains the background script that listens for events and captures the product page URL for analysis.

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "getProductUrl") {
        const productUrl = window.location.href;
        sendResponse({ url: productUrl });
    }
});

chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
    if (changeInfo.status === 'complete' && tab.url) {
        chrome.tabs.sendMessage(tabId, { action: "pageLoaded", url: tab.url });
    }
});