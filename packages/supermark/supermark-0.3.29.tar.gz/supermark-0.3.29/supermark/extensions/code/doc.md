Syntax highlighting for code.

# Code Blocks

Supermark  uses Pandoc's functions to highlight code. Place the code between the following delimiters:


<div>
<pre>
```bash
pandoc --list-highlight-languages
```
</pre>
</div>


`abc`, `asn1`, `asp`, `ats`, `awk`, `actionscript`, `ada`, `agda`, `alertindent`, `apache`, `bash`, `bibtex`, `boo`, `c`, `cs`, `cpp`, `cmake`, `css`, `changelog`, `clojure`, `coffee`, `coldfusion`, `commonlisp`, `curry`, `d`, `dtd`, `diff`, `djangotemplate`, `dockerfile`, `doxygen`, `doxygenlua`, `eiffel`, `elixir`, `email`, `erlang`, `fsharp`, `fortran`, `gcc`, `glsl`, `gnuassembler`, `m4`, `go`, `html`, `hamlet`, `haskell`, `haxe`, `ini`, `isocpp`, `idris`, `fasm`, `nasm`, `json`, `jsp`, `java`, `javascript`, `javadoc`, `julia`, `kotlin`, `llvm`, `latex`, `lex`, `lilypond`, `literatecurry`, `literatehaskell`, `lua`, `mips`, `makefile`, `markdown`, `mathematica`, `matlab`, `maxima`, `mediawiki`, `metafont`, `modelines`, `modula2`, `modula3`, `monobasic`, `ocaml`, `objectivec`, `objectivecpp`, `octave`, `opencl`, `php`, `povray`, `pascal`, `perl`, `pike`, `postscript`, `powershell`, `prolog`, `pure`, `purebasic`, `python`, `r`, `relaxng`, `relaxngcompact`, `roff`, `ruby`, `rhtml`, `rust`, `sgml`, `sql`, `sqlmysql`, `sqlpostgresql`, `scala`, `scheme`, `tcl`, `tcsh`, `texinfo`, `mandoc`, `vhdl`, `verilog`, `xml`, `xul`, `yaml`, `yacc`, `zsh`, `dot`, `noweb`, `rest`, `sci`, `sed`, `xorg`, `xslt`,

For an updated list, type:

```bash
pandoc --list-highlight-languages
```