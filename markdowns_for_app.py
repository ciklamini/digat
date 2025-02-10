# -*- coding: utf-8 -*-



def get_intro_markdown()->str:
    return '''
    ## Introduction to wave analysis:

    This app has function to see 3D tracks to furher explore possibility \
        on wave movements.
    Preprint is available on: < url >

   '''
def get_wrapper_markdown()->str:
    return '''
    ...
    This example uses the block delimiter:
    $$
    \\frac{1}{(\\sqrt{\\phi \\sqrt{5}}-\\phi) e^{\\frac25 \\pi}} =
    1+\\frac{e^{-2\\pi}} {1+\\frac{e^{-4\\pi}} {1+\\frac{e^{-6\\pi}}
    {1+\\frac{e^{-8\\pi}} {1+\\ldots} } } }
    $$

    This example uses the inline delimiter:
    $E^2=m^2c^4+p^2c^2$

    ## LaTeX in a Graph component:


    '''
    
def get_description_markdown()->str:
    return '''
    ## 
    
    This page is dedicated to handling EMT file uploads for visualizing tracking points
    from laboratory experiments. Users can drop EMT files here to see experimental data
    represented through dynamic tracking visualizations.
    LaTeX in a Markdown component:

    '''
    
