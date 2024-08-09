__all__ = ["tailwind"]

from typing import Optional
from .core.ext import zyxModuleLoader

class TailwindManager:
    """
    A manager class for handling Tailwind CSS and React client integration in Jupyter notebooks.
    """

    initialized = False

    def __init__(self, className: Optional[str] = None):
        self.className = className if className is not None else ""
        if not TailwindManager.initialized:
            self.setup_environment()
            TailwindManager.initialized = True

    def setup_environment(self):
        """
        Set up Tailwind CSS, React, and custom fonts. Ensures that they are loaded only once.
        """
        setup_scripts = """
        <!DOCTYPE html>
        <html>
        <head>
            <script>
                require.config({
                    paths: {
                        'react': 'https://unpkg.com/react@17/umd/react.production.min',
                        'react-dom': 'https://unpkg.com/react-dom@17/umd/react-dom.production.min'
                    }
                });

                require(['react', 'react-dom'], function(React, ReactDOM) {
                    window.React = React;
                    window.ReactDOM = ReactDOM;

                    var script = document.createElement('script');
                    script.src = 'https://cdn.tailwindcss.com';
                    script.onload = function() {
                        tailwind.config = {
                            theme: {
                                extend: {
                                    fontFamily: {
                                        'dm-sans': ['DM Sans', 'sans-serif'],
                                        'lora': ['Lora', 'serif'],
                                        'jetbrains-mono': ['JetBrains Mono', 'monospace'],
                                    },
                                },
                            },
                        };

                        var style = document.createElement('style');
                        style.textContent = `
                            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Lora:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
                            
                            .jp-RenderedHTMLCommon { font-family: 'DM Sans', sans-serif; }
                            .jp-RenderedHTMLCommon h1, 
                            .jp-RenderedHTMLCommon h2, 
                            .jp-RenderedHTMLCommon h3, 
                            .jp-RenderedHTMLCommon h4, 
                            .jp-RenderedHTMLCommon h5, 
                            .jp-RenderedHTMLCommon h6 { font-family: 'Lora', serif; }
                            .jp-RenderedHTMLCommon code, 
                            .jp-RenderedHTMLCommon pre { font-family: 'JetBrains Mono', monospace; }
                        `;
                        document.head.appendChild(style);
                    };
                    document.head.appendChild(script);
                });
            </script>
        </head>
        </html>
        """
        try:
            from IPython.display import display, HTML
        except ImportError:
            raise ImportError("""This module requires IPython to be installed, which is not included in the 'zyx' base package.
                                 Please install it by running:
                                 '! pip install IPython' -- in your notebook
                                 'pip install ipython' -- in your terminal
                              """)
        display(HTML(setup_scripts))

    def display(
        self,
        content: str,
        className: Optional[str] = "",
        component: Optional[str] = "div",
    ):
        """
        Display the HTML element with the specified content, component type, and Tailwind CSS class.
        """
        element = f"<{component} class='{className}'>{content}</{component}>"
        if self.className:
            content = f"<div class='{self.className}'>{element}</div>"
        else:
            content = element
        html = f"<!DOCTYPE html><html><body>{content}</body></html>"
        try:
            from IPython.display import display, HTML
        except ImportError:
            raise ImportError("""This module requires IPython to be installed, which is not included in the 'zyx' base package.
                                 Please install it by running:
                                 '! pip install IPython' -- in your notebook
                                 'pip install ipython' -- in your terminal
                              """)
        display(HTML(html))

_tailwind_manager = None

def tailwind_manager(
    className: Optional[str] = None,
):
    """
    Create a TailwindManager instance with the specified class name.
    """
    global _tailwind_manager
    if _tailwind_manager is None:
        _tailwind_manager = TailwindManager(className)
    return _tailwind_manager

class tailwind(zyxModuleLoader):
    """
    Tailwind class that initializes and loads Tailwind CSS and React.
    """

    pass
tailwind.init("zyx.notebook", "tailwind_manager")
