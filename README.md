> @Date    : 2020-01-17 19:20:00
>
> @Author  : Lewis Tian (taseikyo@gmail.com)
>
> @Link    : github.com/taseikyo

![Sublime Markdown Helper](https://socialify.git.ci/taseikyo/sublime-markdown-helper/image?forks=1&issues=1&language=1&owner=1&pattern=Brick%20Wall&pulls=1&stargazers=1&theme=Light)

A simple Sublime Text 3 plugin can help you write Markdown faster.

I am new to the st3 plugin, and my motivation is to focus on text rather than Markdown syntax. My task is to write the text, and the rest of the work is done by the plugin, which converts the plain text into a markdown document.

## preview

![preview](images/preview.gif)

## how to use

Go to Preferences -> Browse Packages, and then either download and unzip this
plugin into that directory, or:

```Bash
cd $ST3Packages
git clone https://github.com/taseikyo/sublime-markdown-helper.git
```

This plugin only works in Markdown files, if you want to add more file types, add them in the "MarkdownHelper.sublime-settings" file.

```Json
{
    "allow_fileformats": [
        "md",
        "markdown",
        // more types..
    ]
}
```

### shortcuts

| Keyboard shortcut |	Description  |
|-------------------|----------------|
|ctrl + 1-3         |h1 - h3         |
|ctrl + 4	        |unordered list  |
|ctrl + shift + 4	|task list       |
|ctrl + 5			|ordered list  	 |
|ctrl + 6			|code (block)    |
|ctrl + shift + 6	|code (inline)   |
|ctrl + 7			|latex formula (block)|
|ctrl + shift + 7	|latex formula (inline)|
|ctrl + b	        |bold            |
|ctrl + shift + d	|deleted         |
|ctrl + i	        |italic          |
|ctrl + m	        |image           |

**Note: Remember to select the entire line before you press the shortcuts. (except for inline code/latex formula, bold, italic, deleted text, and image)**

For Mac users: ctrl -> cmd, shift -> option

## License

Copyright (c) 2020 Lewis Tian. Licensed under the MIT license.
