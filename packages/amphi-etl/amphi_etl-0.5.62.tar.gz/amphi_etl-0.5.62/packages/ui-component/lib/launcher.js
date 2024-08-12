import { Launcher as JupyterlabLauncher, LauncherModel as JupyterLauncherModel } from '@jupyterlab/launcher';
import { githubIcon, pipelineIcon, slackIcon, alertDiamondIcon } from './icons';
import { each } from '@lumino/algorithm';
import React, { useEffect, useState } from 'react';
// Largely inspired by Elyra launcher https://github.com/elyra-ai/elyra
/**
 * The known categories of launcher items and their default ordering.
 */
const AMPHI_CATEGORY = 'Data Integration';
const CommandIDs = {
    newPipeline: 'pipeline-editor:create-new',
    newFile: 'fileeditor:create-new',
    createNewPythonEditor: 'script-editor:create-new-python-editor',
    createNewREditor: 'script-editor:create-new-r-editor'
};
// LauncherModel deals with the underlying data and logic of the launcher (what items are available, their order, etc.).
export class LauncherModel extends JupyterLauncherModel {
    /**
     * Return an iterator of launcher items, but remove unnecessary items.
     */
    items() {
        const items = [];
        let pyEditorInstalled = false;
        let rEditorInstalled = false;
        this.itemsList.forEach(item => {
            if (item.command === CommandIDs.createNewPythonEditor) {
                pyEditorInstalled = true;
            }
            else if (item.command === CommandIDs.createNewREditor) {
                rEditorInstalled = true;
            }
        });
        if (!pyEditorInstalled && !rEditorInstalled) {
            return this.itemsList[Symbol.iterator]();
        }
        // Dont add tiles for new py and r files if their script editor is installed
        this.itemsList.forEach(item => {
            var _a, _b;
            if (!(item.command === CommandIDs.newFile &&
                ((pyEditorInstalled && ((_a = item.args) === null || _a === void 0 ? void 0 : _a.fileExt) === 'py') ||
                    (rEditorInstalled && ((_b = item.args) === null || _b === void 0 ? void 0 : _b.fileExt) === 'r')))) {
                items.push(item);
            }
        });
        return items[Symbol.iterator]();
    }
}
// Launcher deals with the visual representation and user interactions of the launcher
// (how items are displayed, icons, categories, etc.).
export class Launcher extends JupyterlabLauncher {
    /**
     * Construct a new launcher widget.
     */
    constructor(options, commands) {
        super(options);
        this.myCommands = commands;
        // this._translator = this.translator.load('jupyterlab');
    }
    /**
    The replaceCategoryIcon function takes a category element and a new icon.
    It then goes through the children of the category to find the section header.
    Within the section header, it identifies the icon (by checking if it's not the section title)
    and replaces it with the new icon. The function then returns a cloned version of the original
    category with the icon replaced.
     */
    replaceCategoryIcon(category, icon) {
        const children = React.Children.map(category.props.children, child => {
            if (child.props.className === 'jp-Launcher-sectionHeader') {
                const grandchildren = React.Children.map(child.props.children, grandchild => {
                    if (grandchild.props.className !== 'jp-Launcher-sectionTitle') {
                        return React.createElement(icon.react, { stylesheet: "launcherSection" });
                    }
                    else {
                        return grandchild;
                    }
                });
                return React.cloneElement(child, child.props, grandchildren);
            }
            else {
                return child;
            }
        });
        return React.cloneElement(category, category.props, children);
    }
    /**
     * Render the launcher to virtual DOM nodes.
     */
    render() {
        // Bail if there is no model.
        if (!this.model) {
            return null;
        }
        // get the rendering from JupyterLab Launcher
        // and resort the categories
        const launcherBody = super.render();
        const launcherContent = launcherBody === null || launcherBody === void 0 ? void 0 : launcherBody.props.children;
        const launcherCategories = launcherContent.props.children;
        const categories = [];
        const knownCategories = [
            AMPHI_CATEGORY,
            //this._translator.__('Console'),
            // this._translator.__('Other'),
            //this._translator.__('Notebook')
        ];
        // Assemble the final ordered list of categories
        // based on knownCategories.
        each(knownCategories, (category, index) => {
            React.Children.forEach(launcherCategories, cat => {
                if (cat.key === category) {
                    if (cat.key === AMPHI_CATEGORY) {
                        cat = this.replaceCategoryIcon(cat, pipelineIcon);
                    }
                    categories.push(cat);
                }
            });
        });
        const handleNewPipelineClick = () => {
            this.myCommands.execute('pipeline-editor:create-new');
        };
        const handleUploadFiles = () => {
            this.myCommands.execute('ui-components:file-upload');
        };
        const AlertBox = () => {
            const [isVisible, setIsVisible] = useState(false);
            useEffect(() => {
                // Check if the alert was previously closed
                const alertClosed = localStorage.getItem('alertClosed') === 'true';
                setIsVisible(!alertClosed);
            }, []);
            const closeAlert = () => {
                setIsVisible(false);
                // Save the state to prevent the alert from showing again
                localStorage.setItem('alertClosed', 'true');
            };
            if (!isVisible)
                return null;
            return (React.createElement("div", { role: "alert", className: "mt-5 rounded-xl border border-gray-100 bg-white p-4" },
                React.createElement("div", { className: "flex items-start gap-4" },
                    React.createElement("span", { className: "text-primary" },
                        React.createElement(alertDiamondIcon.react, null)),
                    React.createElement("div", { className: "flex-1" },
                        React.createElement("h2", { className: "block font-bold text-black-900" }, "About"),
                        React.createElement("p", { className: "mt-1 text-sm text-gray-700" },
                            "Welcome to Amphi's demo playground! Explore Amphi ETL's capabilities and user experience here. ",
                            React.createElement("br", null),
                            "Note that ",
                            React.createElement("b", null, "executing pipelines is not supported in this environment. "),
                            "For full functionality, install Amphi \u2014 it's free and open source. ",
                            React.createElement("a", { href: "https://github.com/amphi-ai/amphi-etl", target: "_blank", className: "text-primary underline" }, "Learn more."))),
                    React.createElement("button", { onClick: closeAlert, className: "text-gray-500 transition hover:text-gray-600" },
                        React.createElement("span", { className: "sr-only" }, "Dismiss popup"),
                        React.createElement("svg", { xmlns: "http://www.w3.org/2000/svg", fill: "none", viewBox: "0 0 24 24", strokeWidth: "1.5", stroke: "currentColor", className: "h-6 w-6" },
                            React.createElement("path", { strokeLinecap: "round", strokeLinejoin: "round", d: "M6 18L18 6M6 6l12 12" }))))));
        };
        // Wrap the sections in body and content divs.
        return (React.createElement("div", { className: "jp-Launcher-body" },
            React.createElement("div", { className: "jp-Launcher-content" },
                React.createElement("h1", { className: "mt-8 text-2xl font-bold sm:text-3xl flex items-center text-gray-900" }, "Amphi ETL"),
                React.createElement("div", { className: "mt-12 grid grid-cols-1 gap-4 lg:grid-cols-2 lg:gap-8" },
                    React.createElement("div", { className: "rounded-sm bg-white p-4" },
                        React.createElement("div", { className: "flex items-center gap-4" },
                            React.createElement("div", null,
                                React.createElement("h3", { className: "text-xl font-bold text-gray-900 sm:text-3xl" }, "Start"),
                                React.createElement("div", { className: "flow-root" },
                                    React.createElement("ul", { className: "-m-1 flex flex-wrap" },
                                        React.createElement("li", { className: "p-1 leading-none" },
                                            React.createElement("a", { href: "https://docs.amphi.ai/category/getting-started", target: "_blank", className: "text-xs font-medium text-primary" }, "Getting Started")))))),
                        React.createElement("ul", { className: "mt-4 space-y-2" },
                            React.createElement("li", null,
                                React.createElement("a", { href: "#", onClick: handleNewPipelineClick, className: "block h-full rounded-sm border border-gray-100 p-4 hover:border-pastel hover:bg-grey flex items-center gap-4" },
                                    React.createElement("div", { className: "flex items-center justify-center w-16 h-16 rounded-full" },
                                        React.createElement(pipelineIcon.react, { fill: "#5A8F7B" })),
                                    React.createElement("div", null,
                                        React.createElement("strong", { className: "font-bold text-primary" }, "New pipeline"),
                                        React.createElement("p", { className: "mt-1 text-xs font-medium" }, "Open a new untitled pipeline and drag and drop components to design and develop your data flow.")))))),
                    React.createElement("div", { className: "rounded-sm bg-white p-4" },
                        React.createElement("div", { className: "flex items-center gap-4" },
                            React.createElement("div", null,
                                React.createElement("h3", { className: "text-xl font-bold text-gray-900 sm:text-3xl" }, "Resources"),
                                React.createElement("div", { className: "flow-root" },
                                    React.createElement("ul", { className: "-m-1 flex flex-wrap" },
                                        React.createElement("li", { className: "p-1 leading-none" },
                                            React.createElement("a", { href: "https://docs.amphi.ai/", target: "_blank", className: "text-xs font-medium text-primary" }, "Documentation")))))),
                        React.createElement("ul", { className: "mt-4 space-y-2" },
                            React.createElement("li", null,
                                React.createElement("a", { href: "https://github.com/amphi-ai/amphi-etl", target: "_blank", className: "block h-full rounded-sm border border-gray-100 p-4 hover:border-pastel hover:bg-grey flex items-center gap-4" },
                                    React.createElement("div", { className: "flex items-center justify-center w-16 h-16 rounded-full" },
                                        React.createElement(githubIcon.react, null)),
                                    React.createElement("div", null,
                                        React.createElement("strong", { className: "font-bold text-primary" }, "Issues and feature requests"),
                                        React.createElement("p", { className: "mt-1 text-xs font-medium" }, "Report issues and suggest features on GitHub. Don't hesitate to star the repository to watch the repository.")))),
                            React.createElement("li", null,
                                React.createElement("a", { href: "https://join.slack.com/t/amphi-ai/shared_invite/zt-2ci2ptvoy-FENw8AW4ISDXUmz8wcd3bw", target: "_blank", className: "block h-full rounded-sm border border-gray-100 p-4 hover:border-pastel hover:bg-grey flex items-center gap-4" },
                                    React.createElement("div", { className: "flex items-center justify-center w-16 h-16 rounded-full" },
                                        React.createElement(slackIcon.react, null)),
                                    React.createElement("div", null,
                                        React.createElement("strong", { className: "font-bold text-primary" }, "Join the Community"),
                                        React.createElement("p", { className: "mt-1 text-xs font-medium" }, "Join Amphi's community on Slack: seek help, ask questions and share your experience."))))))))));
    }
}
