project(gen-code)

set(BisonOutput_s snazzle.tab.cpp)
set(BisonOutput_h snazzle.tab.h)

set(FlexOutput lex.yy.c)

add_custom_command(
    OUTPUT 
    ${BisonOutput_s}
    ${FlexOutput}
    COMMAND win_bison --defines=${BisonOutput_h} --output=${BisonOutput_s} "${CMAKE_CURRENT_SOURCE_DIR}/snazzle.y"
    COMMAND win_flex --wincompat --noyywrap --outfile=${FlexOutput} "${CMAKE_CURRENT_SOURCE_DIR}/snazzle.l"
    COMMENT "Generating files"
)

set_source_files_properties(${FlexOutput} PROPERTIES LANGUAGE CXX )

add_library(${PROJECT_NAME} STATIC ${BisonOutput_s} ${FlexOutput})