set nocompatible

nnoremap <CR>   <Esc>:w<CR>i

"改变不同模式下光标的颜色
let &t_SI.="\e[5 q" "SI = INSERT mode
let &t_SR.="\e[4 q" "SR = REPLACE mode
let &t_EI.="\e[1 q" "EI = NORMAL mode (ELSE)


" 光标所在行列高亮
"set cursorcolumn
"set cursorline

" 插入模式下underline,s
:autocmd InsertEnter * set cul
:autocmd InsertLeave * set nocul

"config: set basic
set backspace=2
set nowrap
set showmatch
set scrolloff=3
set encoding=utf-8
set fenc=utf-8
set mouse=a
set hlsearch
syntax on
set nu
set tabstop=4
set shiftwidth=4
set softtabstop=4
set autochdir
set mouse=a
set autoindent
set smartindent
set cindent


"set highlight
"highlight CursorLine   cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE
"highlight CursorColumn cterm=NONE ctermbg=black ctermfg=green guibg=NONE guifg=NONE
