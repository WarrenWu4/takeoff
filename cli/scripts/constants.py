class Constants:
    TAILWIND_CONFIG = """
    /** @type {import('tailwindcss').Config} */
    export default {
        content: [
            "./index.html",
            "./src/**/*.{js,ts,jsx,tsx}",
            ],
        theme: {
            extend: {},
            },
        plugins: [],
    }
    """
    TAILWIND_INDEXCSS = """
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    """


