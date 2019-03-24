\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{nsfproposal}[2016/08/01 based on NSF proposal style gpg16001]
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions
\LoadClass[11pt]{article}
\RequirePackage{calc}
%\RequirePackage{natbib}
\RequirePackage[american]{babel}
%\RequirePackage{hyperref} % handled by pandoc
\RequirePackage{mathpazo}
\RequirePackage{graphicx,xcolor}
\RequirePackage{sectsty,titlecaps}
\RequirePackage{enumitem}
\setlist{nosep}
\usepackage[export]{adjustbox}

\setlength{\paperheight}{11in}
\setlength{\paperwidth}{8.5in}
\addtolength{\voffset}{-1in}
\addtolength{\hoffset}{-1in}
\setlength{\topmargin}{0in}
\setlength{\oddsidemargin}{1in}
\setlength{\evensidemargin}{1in}
\setlength{\textwidth}{\paperwidth - 2in}
\setlength{\textheight}{\paperheight - 2in}
\setlength{\footskip}{36pt}
\setlength{\marginparsep}{0.5cm}
\setlength{\marginparwidth}{1.5cm}
\setlength{\headheight}{0.7 in} % .75 in}
\setlength{\headsep}{0.3 in}


%----------------------------------------------------------------------
%	SECTION/SUBSECTION/PARAGRAPH SET-UP
%----------------------------------------------------------------------

\definecolor{color1}{RGB}{0,0,0} % Color of the article title and sections
\definecolor{color2}{RGB}{255,255,255} % Color of the boxes behind the abstract and headings

\RequirePackage[explicit]{titlesec}
\titleformat{\section} %section title format
  {\color{color1}\small\sffamily\bfseries}
  {}
  {0em}
  {\arabic{section}. \MakeUppercase{#1}}
  []
\titleformat{name=\section,numberless} % numberless section title format
  {\color{color1}\small\sffamily\bfseries}
  {}
  {0em}
  {\MakeUppercase{#1}}
  []  
\titleformat{\subsection}
  {\color{color1}\sffamily}
  {\thesubsection}
  {0.5em}
  {\underline{\smash{\titlecap{#1}}}}
  []
\titleformat{\subsubsection}
  {\sffamily}
  {\thesubsubsection}
  {0.5em}
  {\textbf{#1}}
  []    
\titleformat{\paragraph}[runin]
  {\sffamily\small\bfseries}
  {}
  {0em}
  {#1} 
\titlespacing*{\section}{0pc}{1pt \@plus1pt \@minus1pt}{1pt}
\titlespacing*{\subsection}{0pc}{-1pt \@plus1pt \@minus1pt}{-1pt}
\titlespacing*{\subsubsection}{0pc}{0ex \@plus1pt \@minus1pt}{0pt}
\titlespacing*{\paragraph}{0pc}{0ex \@plus1pt \@minus1pt}{0pt}

\RequirePackage{fancyhdr}
\pagestyle{fancyplain}
\renewcommand{\headrulewidth}{0pt}
% Headers
\lhead{\color{color1!50}\sffamily \LeftHeader}%
\chead{\color{color1!50}\sffamily \MiddleHeader}%
\rhead{\color{color1!50}\sffamily \RightHeader}%
% Footers
\lfoot{\color{color1!50}\sffamily \LeftFooter}%
\cfoot{}%
\newcounter{offsetpage}
\setcounter{offsetpage}{1}
\rfoot{\ifnum\value{page}>\PageLimit \color{color1!50}\sffamily Page \arabic{page} \else \color{color1!50}\sffamily Page \arabic{page}\toPageLimit \fi}%

\renewcommand\floatpagefraction{.9}
