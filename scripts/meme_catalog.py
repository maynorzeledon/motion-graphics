"""Static meme layouts, reusable templates, and reply media collections."""
REFERENCE_ID='styles-and-inspiration/social-post-and-meme-styles/meme-news-cards/user-reference-portrait-and-bold-headline'
def extend_memes(group):
 group('Styles and inspiration','Social post and meme styles','Meme-news cards','User reference — portrait and bold headline|Photo with black gradient headline|Condensed all-caps headline|White headline with bright accent words|Viral corner badge|Question footer|Photo-first news card|Headline-first news card|Two-image comparison news card|Carousel story recap')
 group('Styles and inspiration','Social post and meme styles','Shitpost and meme editing','Deliberately rough collage|Deep-fried compression|Oversized ironic captions|Low-resolution image macro|Surreal unrelated image pairing|Deliberately awkward cropping|Screenshot-with-reaction layout|Fake desktop dialogue parody|Chaotic sticker layering|Absurd comparison panel|Deadpan text over ordinary photo|Anti-design poster')
 group('Styles and inspiration','Social post and meme styles','Static social layouts','Photo plus punchline|Text-only joke card|Chat screenshot parody|Comment screenshot card|Reddit-style story card|Quote-and-reaction image|Two-panel visual joke|Four-panel story|Polished satire card|Cropped screenshot caption')
 sections={
 'Classic template families':{
 'Image macros':'Top-text bottom-text blank|Single-caption image blank|Caption-above-photo blank|Caption-below-photo blank|Impact-style text placement|Outlined text variant',
 'Comparison and choice':'Drake-style two-choice study|Distracted-boyfriend-style object labels|Two-buttons dilemma study|Expectation versus reality|Before versus after|Same energy comparison|Correct versus incorrect comparison',
 'Escalation and sequences':'Expanding-brain-style sequence|Increasingly intense reaction|Domino chain labels|Three-stage escalation|Four-panel comic blank|Setup → reaction → payoff',
 'Characters and reactions':'Wojak-style character template target|Doge-style caption target|Side-eye character blank|Thinking character blank|Confused character blank|Celebrating character blank|Disappointed character blank'},
 'Text and wordplay templates':{
 'Caption formats':'Nobody / absolutely nobody format|Me versus my brain format|POV setup|When someone says format|My honest reaction format|One-word caption|Overly specific scenario|Literal interpretation caption',
 'Dialogue and labels':'Two-character dialogue|Inner monologue|Object-labeling blank|Speech bubble slots|Thought bubble slots|Chat dialogue blank|Comment-and-response blank',
 'Absurdist and shitpost blanks':'Unrelated image plus serious caption|Over-explained ordinary image|Intentionally bad motivational quote|Ironic infographic|Nonsense comparison|Fake instruction parody|Deliberately useless diagram|Surreal news-card blank'},
 'Meme-news and satire templates':{
 'Headline cards':'Portrait-plus-headline blank|Accent-word headline slots|Viral badge blank|Breaking-news parody card|Image plus source strip|Question footer blank|Multi-slide headline story',
 'Editorial ingredients':'Background photo slot|Subject crop slot|Black gradient overlay|Headline line-break guide|Accent-word selection|Category badge slot|Brand footer slot|Source/date slot',
 'Context records':'Original source screenshot|Headline status record|Verified-story source pointer|Satire/parody label record|Image provenance note|Editable text layer record'},
 'Reusable files and variants':{
 'Template packages':'Blank base image|Editable SVG template|Layered PSD reference|Editable design source|Caption-slot manifest|Example finished meme|Font/source record|Crop-safe preview',
 'Delivery sizes':'Square feed template|Portrait feed template|Vertical story template|Landscape reaction image|Transparent cutout|Light-background variant|Dark-background variant',
 'Organization':'Template name and aliases|Caption fields|Emotion tags|Intended joke structure|Example usage context|Original creator/source|License/usage notes|Related reaction assets'}
 }
 for section,families in sections.items():
  for name,items in families.items():group('Meme templates',section,name,items)
 reactions={
 'Emotion and intent':{
 'Reaction moods':'Laughing|Confused|Shocked|Side-eye|Disbelief|Facepalm|Approval|Disapproval|Celebration|Relief|Embarrassment|Awkward silence|Sadness|Frustration|Anticipation|Mind blown',
 'Conversational intent':'Agree with parent comment|Playful disbelief|Say thank you|Congratulate someone|Show appreciation|Ask for an explanation|Continue a joke|React to a reveal|Gentle disagreement|Supportive reaction'},
 'GIF and animation formats':{
 'Looping reactions':'Seamless reaction loop|One-shot reaction|Short reaction then hold|Progressively zoomed reaction|Reaction with caption|Silent expression loop|Animated emote|Transparent animated sticker',
 'File types':'GIF source|Animated WebP|Animated PNG|Short MP4|Transparent WebM|Static fallback frame|First-frame preview|Contact sheet',
 'Timing and legibility':'Reaction onset marker|Punchline frame|Loop duration|Hold duration|Caption-readable version|Reduced-flash version|Compact mobile version'},
 'Reply images and stickers':{
 'Image reactions':'Reaction photograph|Reaction illustration|Text reaction image|Quote-and-reaction image|Meme-panel crop|Screenshot reaction|Emoji collage|Tiny reaction image',
 'Sticker families':'Transparent person cutout|Transparent animal reaction|Cartoon reaction target|Mascot expression|Hand gesture|Speech bubble sticker|Text-only sticker|Celebration sticker|Question sticker|Arrow and emphasis sticker',
 'Characters and subjects':'Human expression|Cat reaction|Dog reaction|Bird reaction|Game-character target|Sports reaction target|Movie/TV reaction target|Original mascot reaction|Simple stickman reaction'},
 'Use and reference records':{
 'Context matching':'Parent comment example|Video moment example|Meaning of reaction|Sincere use example|Sarcastic use example|When the reaction would misread the tone|Language/culture notes',
 'Source and collection':'Original source link|Creator/source credit|Full-context reference|Reaction crop|Caption transcript|Upload file|Preview thumbnail|Tags and aliases|Usage/license record',
 'Platform delivery studies':'Instagram reply reference|TikTok reply reference|YouTube reply reference|Reddit reaction reference|Messaging sticker reference|Discord emote reference|Small-size readability|Transparent-edge check'}
 }
 for section,families in reactions.items():
  for name,items in families.items():group('Reply GIFs, images and stickers',section,name,items)
def enrich_memes(catalog):
 def visit(node):
  if node['id']==REFERENCE_ID:
   node.update(status='reference',preview='references/meme-news/user-meme-news-reference.jpeg',attachmentCount=1,files=[{'path':'references/meme-news/user-meme-news-reference.jpeg','name':'User-supplied meme-news screenshot','role':'Editing reference'}],notes='User-supplied layout reference. Portrait photo at top; black gradient behind bold white condensed all-caps headline; vivid pink emphasis words and corner VIRAL badge; compact question/footer. Save as a visual layout reference. The screenshot headline is unverified and is not evidence about the pictured person.',license='User-supplied screenshot; original publisher and image rights not established. Reference use recorded; no stock-photo license claimed.')
  for child in node.get('children',[]):visit(child)
 for category in catalog['categories']:visit(category)
