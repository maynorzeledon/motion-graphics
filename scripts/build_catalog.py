"""Curate taxonomy here; regenerate dist/catalog.json with Python 3."""
import json, re, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
T={}
def group(category, section, name, items):
    T.setdefault(category,{}).setdefault(section,{})[name]=items.split('|')
# INTERACTION AND INTERFACES
for name,items in {
'Toggles':'Basic on/off|Spring toggle|Day/night toggle|Icon morph toggle|Liquid toggle|Segmented toggle|Checkbox switch|Theme switch|Sound toggle|3D rocker switch',
'Loading':'Spinner|Bouncing dots|Skeleton shimmer|Progress ring|Progress bar|Percentage counter|Liquid fill|Logo loader|Circular orbit|Indeterminate bar|File upload progress|Download progress|Success completion',
'Dropdowns and selection':'Dropdown open/close|Searchable select|Multi-select chips|Nested menu|Radio selection|Checkbox checkmark|Country selector|Language selector|Command palette|Combobox results|Context menu|Date selection',
'Sliders':'Volume slider|Brightness slider|Range selector|Stepped slider|Color slider|Timeline scrubber|Drag handle|Spring thumb|Tooltip value|Before/after slider',
'Buttons':'Hover fill|Magnetic button|Press depth|Ripple click|Loading to success|Icon button|Floating action button|Hold to confirm|Destructive confirmation|Share expansion',
'Cards and panels':'Card flip|Card stack|Accordion|Expandable card|Glass panel|Tilt hover|Drag reorder|Carousel|Swipe dismiss|Bottom sheet|Modal dialog|Side drawer',
'Navigation':'Tab underline|Pill tab|Sidebar collapse|Breadcrumb transition|Page indicator|Hamburger to close|Dock magnification|Radial menu|Pagination|Scroll progress',
'Notifications':'Toast slide|Notification stack|Badge count|Bell ring|Push banner|Permission prompt|Error shake|Success check|Inline validation|Undo snackbar',
'Input and feedback':'Typing cursor|Text selection|Autocomplete|Password reveal|OTP input|Search focus|Form validation|Copy feedback|Drag and drop|Pull to refresh|Empty state|Offline state'
}.items():group('Animations','Interface controls',name,items)
platforms={
'Instagram':'Feed post|Story progress|Story transition|Reels player|Like heart|Comments drawer|DM conversation|Profile grid|Follow button|Save post|Share sheet|Live badges',
'TikTok':'Vertical feed|Like burst|Comment sheet|Follow badge|Caption reveal|Music ticker|Profile screen|Live overlay|Search results|Record controls',
'Spotify':'Now playing|Album art transition|Queue reorder|Playlist scroll|Lyrics highlight|Play/pause morph|Seek bar|Audio waveform|Library grid|Wrapped cards|Device picker',
'YouTube':'Subscribe button|Notification bell|Video player|Timeline hover|Chapter markers|Comment thread|Shorts feed|Channel page|End screen|Like counter|Mini player',
'iPhone / iOS':'Dynamic Island expand|Lock screen|Home screen|App launch|Control Center|Notification Center|Keyboard typing|Safari tabs|Messages bubbles|FaceTime call|App switcher|Widgets|Face ID|Battery charging|Live Activity',
'Samsung / Android':'One UI home|Quick settings|Notification shade|Android keyboard|App drawer|Recent apps|Edge panel|Incoming call|Material button|Material sheet|Charging screen|Permission dialog',
'macOS':'Dock hover|Finder window|Window minimize|Spotlight|Menu bar|Desktop switch|Traffic light controls|Terminal typing|Stage Manager|Notification panel',
'Windows':'Start menu|Taskbar|Snap layout|File Explorer|Window maximize|Search panel|Quick settings|Notification panel|Terminal|Desktop switch',
'Browser':'Address bar typing|Tab open/close|Tab grouping|Bookmarks|Page scroll|Search suggestions|Download panel|Security indicator|DevTools|Responsive preview|Cookie banner|Back navigation',
'Calendar':'Month view|Week view|Day view|Event creation|Event drag|Date flip|Reminder pop|Availability grid|Meeting invitation|Time zone view',
'Widgets':'Weather card|Clock widget|Battery widget|Activity rings|News widget|Music widget|Calendar widget|Habit tracker|Stock ticker|Photo widget',
'ChatGPT':'Prompt typing|Message stream|Thinking state|Voice orb|Attachment chip|Conversation sidebar|Code block|Tool result|Model selector|Canvas panel',
'Claude':'Prompt composer|Streaming reply|Artifact panel|Project selector|File attachment|Code preview|Conversation list|Thinking disclosure',
'Gemini':'Prompt input|Response reveal|Model switch|File attachment|Voice input|Result card|Conversation list',
'Grok':'Chat input|Streaming response|Search sources|Voice interface|Result cards|Conversation panel',
'X / Twitter':'Tweet compose|Post card|Repost|Like burst|Thread expansion|Poll|Notifications|Profile|Spaces audio',
'Reddit':'Post card|Upvote counter|Nested comments|Subreddit header|Award|Flair selection|Feed sort|Image gallery',
'Facebook':'Feed card|Reaction picker|Comment expansion|Messenger bubble|Story|Profile cover|Share dialog|Event card',
'Pinterest':'Masonry grid|Pin zoom|Save board selector|Board reveal|Search suggestions|Related pins|Video pin player',
'Snapchat':'Camera controls|Chat list|Snap opening|Story carousel|Map avatar|Lens selector|Streak badge',
'Google Workspace':'Gmail inbox|Gmail compose|Docs typing|Docs comment|Sheets cell selection|Sheets chart|Slides transition|Drive file grid|Meet call|Forms response',
'Microsoft 365':'Outlook inbox|Word typing|Excel range highlight|PowerPoint slide|Teams chat|Teams meeting|OneDrive upload|OneNote page',
'Camera':'Focus reticle|Shutter flash|Zoom dial|Lens switch|Recording timer|Exposure slider|Portrait depth|Camera grid',
'Photo Gallery':'Photo grid|Pinch zoom|Shared element photo|Album opening|Scrub carousel|Selection check|Edit sliders|Before/after edit',
'App Store':'App card|Install progress|Open button|Ratings reveal|Screenshot carousel|Search results|Subscription sheet',
'Play Store':'App listing|Install progress|Category tabs|Ratings chart|Screenshot carousel|Search results|Update list',
'CapCut':'Timeline edit|Clip split|Caption track|Effects picker|Keyframe panel|Export progress',
'After Effects':'Timeline layers|Keyframe graph|Composition panel|Effects controls|Mask path|Render queue',
'DaVinci Resolve':'Edit timeline|Color wheels|Node graph|Waveform scopes|Fusion nodes|Deliver progress',
'Premiere Pro':'Timeline tracks|Source monitor|Program monitor|Effect controls|Audio meters|Export screen',
'Duolingo':'Lesson path|Answer feedback|XP burst|Streak flame|Hearts refill|League promotion|Lesson completion|Mascot reaction',
'Netflix':'Title browse|Hero preview|Profile chooser|Continue watching|Episode list|Player controls|Title reveal',
'Disney+':'Brand row|Title carousel|Profile chooser|Detail page|Player controls|Watchlist save',
'Amazon':'Product card|Cart update|Buy button|Delivery tracking|Review stars|Search results|Prime Video player',
'GitHub':'Contribution grid|Commit graph|Code diff|Pull request card|Issue board|Star counter|Repository tree|Action progress'
}
for name,items in platforms.items():group('Animations','App and operating system UI',name,items)
for name,items in {
'Text reveals':'Word pop|Character stagger|Line mask|Typewriter|Blur reveal|Split word|Letter scramble|Tracking expand|Outline to fill|Gradient text|Handwriting|Text on path|Karaoke highlight|Caption emphasis|Number to word morph',
'Numbers and symbols':'Odometer|Rolling counter|Countdown|Count up|Currency tally|Percentage|Scoreboard|Date flip|Equation build|Timer|Fraction morph|Ticker|Price change',
'Writing tools':'Pen drawing|Pencil sketch|Feather quill|Marker underline|Highlighter stroke|Signature|Ink spread|Eraser wipe|Notebook writing',
'Layouts':'Headline stack|Quote card|Lower third|Title card|Credits roll|Chapter opener|Footnote reveal|Source citation|List build|Comparison labels'
}.items():group('Animations','Typography and writing',name,items)
for name,items in {
'Nature and space':'Butterfly flight|Pigeon flight|Rose bloom|Tree growth|Leaf fall|Moon phases|Sunrise|Earth rotation|Planet orbit|Solar system|Universe zoom|Cloud drift|Rain|Snow|Lightning|Ocean wave',
'Objects and symbols':'Watch hands|Clock tick|Heart pulse|Crown reveal|Light bulb idea|Painting frame reveal|Door open|Ladder climb|Arrow draw|Arrow loop|Music disc spin|Vinyl turntable|Music player|Balance scale|Camera shutter',
'Characters and anatomy':'Brain pulse|Neural connection|Stickman walk|Stickman run|Stickman jump|Stickman fall|Stickman gesture|Eyes blink|Eyes track|Moods change|Face expression|Hand pointing|Heartbeat trace|Breathing loop',
'Particles and materials':'Confetti|Raining money|Dust motes|Sparkles|Smoke|Fire|Water splash|Liquid pour|Liquid morph|Bubbles|Sparks|Snow globe|Sand flow|Flocking particles|Magnetic particles|Energy trail',
'Backgrounds':'Animated mesh gradient|Aurora|Noise field|Dot grid|Moving lines|Wave bands|Abstract blobs|Starfield|Light rays|Bokeh|Parallax landscape|Paper texture drift|Retro grid|Fluid gradient'
}.items():group('Animations','Objects, nature and characters',name,items)
for name,items in {
'Charts':'Bar chart|Grouped bar|Stacked bar|Horizontal bar|Line chart|Area chart|Pie chart|Donut chart|Scatter plot|Bubble chart|Radar chart|Waterfall chart|Sankey diagram|Treemap|Heatmap|Histogram|Box plot|Gantt chart|Candlestick|Waffle chart',
'Graphs and explanation':'Node network|Tree diagram|Flowchart|Timeline|Process steps|Decision tree|Comparison table|Ranking race|Before/after|Cause and effect|Equation walkthrough|Annotated screenshot|News headline stack|Newspaper collage',
'Data motion':'Axis draw|Data point reveal|Live updating value|Sorting bars|Zoom to data|Tooltip follow|Legend filter|Series highlight|Threshold crossing|Missing data gap|Dataset morph|Source label'
}.items():group('Animations','Data and explanation',name,items)
# MAPS
for name,items in {
'World and projection':'Flat world map|Orthographic globe|Mercator view|Equal Earth view|Robinson view|Equirectangular texture|Polar projection|Regional inset|Antimeridian crossing|Globe to flat morph',
'Visual layers':'Political map|Terrain relief|Satellite imagery|Road map|Topographic contours|Bathymetry|Night lights|Land cover|Population density|Weather radar|Temperature field|Historic map|Minimal outline|3D extruded map',
'Borders and places':'Country borders|Disputed boundaries|Historical borders|US state borders|US county borders|Canadian provinces|European regions|City districts|Capital labels|City labels|Country labels|Place markers|Coordinate grid|Scale bar|Compass',
'Transport networks':'Major roads|Motorways|Local streets|Railways|Metro lines|High speed rail|Airports|Flight arcs|Live flight data adapter|Shipping lanes|Ports|Ferry routes|Cycling routes|Walking routes|Bridges and tunnels',
'Physical geography':'Rivers|Lakes|Coastlines|Mountain ranges|Elevation|Deserts|Forests|Volcanoes|Tectonic plates|Ocean currents|Watersheds|Ice coverage|Time zones',
'Animated moves':'Globe spin|Country zoom|City flyover|Orbit camera|Tilt to terrain|Route draw|Moving vehicle|Pulsing marker|Region highlight|Border trace|Choropleth change|Migration flows|Trade flows|Map wipe|Multi-stop trip|Camera match cut',
'Controls and variants':'Layer switcher|Projection switcher|Time slider|Label density|Route editor|Color legend|Custom region|Dark map|Light map|Transparent map|Portrait framing|Landscape framing|Square framing',
'Data preparation':'GeoJSON countries|TopoJSON simplification|Vector tile source|Raster tile source|Digital elevation model|Coordinate conversion|Boundary versioning|Attribution display|Offline cache|Route dataset|Flight dataset|Rail dataset'
}.items():group('Maps and geography','Map system',name,items)
# ASSETS
for name,items in {
'Devices':'iPhone front|iPhone back|iPhone side|iPhone frame|Samsung phone front|Samsung foldable|Android phone|iPad|Android tablet|MacBook|Windows laptop|Desktop monitor|Smartwatch|Headphones|Earbuds|Microphone|Camera|Game controller|VR headset',
'People and characters':'Stickman poses|Hand gestures|Face expressions|Body silhouettes|Crowd silhouettes|Avatar parts|Character turnaround|Mouth shapes|Eye shapes|Mascot poses|Walk cycle frames|Speech bubbles',
'Objects':'Heart|Rose|Crown|Pigeon|Butterfly|Light bulb|Clock|Watch|Ladder|Door|Frame|Pen|Pencil|Feather|Books|Newspaper|Money notes|Coins|Vinyl record|Turntable|Speaker|Scale|Keys|Gift|Shopping bag',
'Environment':'Trees|Leaves|Flowers|Clouds|Mountains|City skyline|Building facades|Rooms|Roads|Rail tracks|Stars|Moon|Sun|Planets|Earth texture|Water texture',
'Interface kits':'Generic mobile kit|Generic desktop kit|Social post kit|Chat kit|Video player kit|Music player kit|Dashboard kit|Browser frame kit|Calendar kit|Widget kit|App icon frames|Cursor pack|Notification kit',
'Icons':'Navigation|Media controls|Files|Communication|Weather|Finance|Health|Education|Technology|Transport|Social logos|Arrows|Status indicators|Settings|Commerce',
'Textures and overlays':'Paper|Film grain|Halftone|Dust|Scratches|Glass|Metal|Fabric|Concrete|Ink|Watercolor|Holographic foil|Light leak|Vignette|Scan lines'
}.items():group('2D assets','Asset packs',name,items)
for name,items in {
'iPhone':'Front/back model|Screen replacement|Camera closeup|Exploded view|Floating spin|Desk placement|Hand holding rig|Multiple phone layout|Color variants|Foldout packaging',
'Samsung and Android':'Galaxy style phone|Foldable open/close|Screen replacement|Camera closeup|Exploded view|Stylus|Color variants|Tablet',
'Computers':'MacBook style laptop|Windows laptop|Laptop hinge rig|Keyboard detail|Screen replacement|Desktop monitor|Desktop tower|Mouse|Trackpad|Mechanical keyboard',
'Audio and wearables':'Over-ear headphones|Earbuds case|Earbuds pair|Speaker|Smartwatch|Watch strap|Microphone|Vinyl turntable|Music disc',
'Objects and scenes':'Logo extrusion|3D icons|Glass shapes|Chrome shapes|Coins|Banknotes|Gift box|Product pedestal|Room|Studio cyclorama|City block|Car|Train|Plane|Satellite|Earth globe',
'Materials':'Glass|Frosted glass|Brushed metal|Chrome|Plastic|Rubber|Paper|Ceramic|Fabric|Liquid|Holographic|Emissive|Clay|Toon',
'Rigging and delivery':'GLB model|GLTF with textures|Blend source|UV textures|PBR texture maps|HDRI lighting|Camera rig|Turntable rig|Exploded assembly rig|LODs|Transparent render|Shadow catcher'
}.items():group('3D assets','Models and production',name,items)
# SOUND AND MUSIC
for name,items in {
'UI feedback':'Click soft|Click mechanical|Toggle on|Toggle off|Pop|Tap|Hover|Selection|Error|Success|Notification|Message sent|Message received|Typing keys|Keyboard space|Backspace|Upload complete|Unlock',
'Movement':'Short whoosh|Long whoosh|Air swipe|Reverse whoosh|Spin|Rise|Fall|Zip|Elastic boing|Spring settle|Glide|Page turn|Paper shuffle|Transition sweep',
'Impacts and emphasis':'Soft thump|Deep hit|Bass drop|Metal hit|Glass tick|Wood knock|Drum accent|Clap|Snap|Punch|Cinematic boom|Sub pulse|Logo sting',
'Nature and ambience':'Fire crackle|Water splash|Rain|Wind|Bird wing|Bird call|Ocean|Forest|City ambience|Room tone|Space hum|Heartbeat|Breathing|Clock tick',
'Technology':'Digital glitch|Data blip|Radar ping|Scanner|Computer startup|Power down|Robot servo|Electric hum|Radio static|Camera shutter|Camera focus|Phone vibration',
'Transition design':'Riser|Downlifter|Reverse cymbal|Cymbal swell|Tape stop|Record scratch|Vinyl crackle|Stutter|Granular sweep|Silence break',
'Voice':'Narration reference|English pronunciation|Spanish pronunciation|Whisper|Announcement|Character voice direction|Breath cleanup|Room tone sample'
}.items():group('Sound effects','Sound families',name,items)
for name,items in {
'Mood':'Uplifting|Curious|Tense|Calm|Triumphant|Playful|Emotional|Mysterious|Dark|Hopeful|Dreamy|Urgent|Elegant',
'Genre':'Ambient|Corporate electronic|Minimal piano|Orchestral|Lo-fi|Synthwave|House|Techno|Hip hop instrumental|Jazz|Acoustic|Percussion|Chiptune|Cinematic hybrid',
'Use and structure':'Explainer bed|Technology demo|Map documentary|Product reveal|Sports montage|News bed|Comedy sting|Intro theme|Outro theme|Seamless loop|Build section|Climax|Quiet section|Logo sonic mark',
'Production files':'Full mix|Instrumental|Drums stem|Bass stem|Melody stem|Atmosphere stem|No melody mix|30 second cut|15 second cut|6 second cut|Loop points|BPM and key|Beat markers'
}.items():group('Music','Music collection',name,items)
# TYPOGRAPHY
for name,items in {
'Sans serif':'Inter|Roboto|Open Sans|Noto Sans|Source Sans 3|IBM Plex Sans|Manrope|DM Sans|Work Sans|Plus Jakarta Sans|Outfit|Space Grotesk|Archivo|Barlow',
'Serif':'Source Serif 4|Noto Serif|Lora|Merriweather|Libre Baskerville|Bodoni Moda|DM Serif Display|Playfair Display|Cormorant Garamond|Instrument Serif',
'Display and condensed':'Bebas Neue|Anton|Oswald|Archivo Black|Barlow Condensed|Teko|Unbounded|Syne|Abril Fatface|Righteous',
'Monospace':'JetBrains Mono|IBM Plex Mono|Fira Code|Roboto Mono|Space Mono|Source Code Pro|Inconsolata',
'Handwritten and playful':'Caveat|Patrick Hand|Kalam|Permanent Marker|Shadows Into Light|Comic Neue|Schoolbell|Architects Daughter',
'Multilingual and symbols':'Spanish accents|Latin extended|Arabic shaping|Devanagari|CJK characters|Emoji fallback|Math symbols|Currency symbols|RTL layout|Noto fallback chain',
'Type systems':'Headline/body pairing|Editorial hierarchy|Caption sizing|Tabular numerals|Variable weight|Variable width|Optical sizing|Italic styles|Font licensing record|WOFF2 web files|OTF source files'
}.items():group('Fonts and typography','Font catalog',name,items)
for name,items in {
'Cuts and spatial':'Hard cut|Match cut|Jump cut|Whip pan|Push|Slide|Zoom through|Camera roll|Parallax transition|Orbit transition|Dolly zoom|Flip|Cube rotation|Portal transition',
'Masks and reveals':'Circle iris|Rectangle wipe|Diagonal wipe|Shape mask|Text mask|Luma wipe|Track matte|Ink reveal|Paint stroke|Paper tear|Page peel|Venetian blinds',
'Optical and texture':'Cross dissolve|Flash frame|Light leak|Lens flare|Motion blur|Directional blur|Radial blur|Depth of field|Chromatic aberration|Film grain|Halation|Bloom|Vignette|Lens distortion',
'Digital and stylized':'Glitch|RGB split|Pixel dissolve|Datamosh reference|Scanline|CRT warp|Halftone|Posterize|Frame echo|Strobe|Stop motion cadence|Rotoscope look|VHS tracking',
'Morph and physics':'Shape morph|Liquid morph|Mesh warp|Displacement|Elastic stretch|Squash and stretch|Spring overshoot|Bounce|Collision|Shatter|Particle dissolve|Cloth reveal',
'Color and finish':'Color grade|Duotone|Gradient map|Color isolate|Exposure ramp|Day/night change|Monochrome|Invert|Saturation pulse|Shadow glow'
}.items():group('Transitions and effects','Effect families',name,items)
# STYLE SYSTEMS
styles={
'Editorial and documentary':{
'Vox-inspired editorial':'Annotated maps|Bold headline hierarchy|Evidence cards|Cutout photo collage|Charts with source notes|Highlighted documents|Editorial pacing',
'Johnny Harris-inspired geography':'Terrain flyover|Travel route|Document overlays|Photo cutouts|Narration-led zoom|Satellite to street|Historical comparison',
'GeoGlobe / globe explainers':'Rotating Earth|Country highlight|Flag callout|Flight arc|Border trace|Fast country zoom|Globe labels',
'Kurzgesagt-inspired illustration':'Flat geometric worlds|Layered vector scenes|Character loops|Cosmic scale comparison|Color-coded systems|Soft texture|Diagram storytelling',
'3Blue1Brown-inspired mathematics':'Equation transformations|Geometric proof|Coordinate animation|Vector field|Number line|Continuous graph change|Concept color coding',
'Veritasium / science documentary':'Physical demonstration|Question opener|Lab annotation|Diagram insert|Experiment comparison|Scale reference|Evidence reveal',
'Fern / cinematic documentary':'Dimensional scene|Atmospheric camera|Dramatic title|Archival collage|Historical reconstruction|Depth parallax|Tension pacing',
'Lemmino-inspired documentary':'Restrained type|Dark maps|Archival sources|Measured pacing|Minimal diagram|Investigation timeline|Ambient score'},
'Product and commercial':{
'Apple-inspired product':'Spacious typography|Material closeup|Floating device|Exploded assembly|Macro camera|Precise easing|Quiet sonic accents',
'Google Material-inspired':'Tonal surfaces|Shape continuity|Shared elements|Expressive spring|Color roles|Container transform|Large rounded type',
'Microsoft Fluent-inspired':'Layered depth|Soft acrylic|Light materials|Icon depth|Window choreography|Subtle glow|Calm transitions',
'Stripe-inspired SaaS':'Gradient fields|Dashboard fragments|Code to outcome|Metric counters|UI choreography|Fine grid|Product storytelling',
'Linear-inspired software':'Dark interface|Tight typography|Smooth UI zoom|Issue cards|Keyboard hints|Subtle gradients|Focused interaction',
'Spotify-inspired music':'Bold color|Album collage|Kinetic type|Beat sync|Wrapped statistics|Expressive shapes|Artist cards',
'Nike-inspired sports':'Fast cuts|Oversized type|Freeze frame|Athlete cutout|High contrast|Impact accents|Rhythmic pacing'},
'Visual languages':{
'Minimalism':'Whitespace|Monochrome|Single accent|Slow motion|Simple shapes|Clean hierarchy',
'Glassmorphism':'Frosted panels|Background blur|Translucent borders|Layered depth|Colored light',
'Neobrutalism':'Heavy outlines|Hard shadows|Bright color|Raw type|Snappy movement',
'Y2K and cyber':'Chrome type|Iridescence|Digital grids|Scanner motifs|Pixel accents',
'Retro analog':'VHS|CRT|Film grain|Print registration|Paper collage|Analog meters',
'Clay and playful 3D':'Clay materials|Rounded objects|Squash|Soft lighting|Toy scale',
'Isometric and 2.5D':'Isometric city|Exploded diagram|Layered cards|Depth extrusion|Parallax illustration',
'Handmade':'Pencil lines|Watercolor|Paper cutout|Stop motion|Handwritten labels',
'Luxury':'Serif headlines|Metallic accents|Slow reveal|Macro textures|Dark studio',
'Anime and manga':'Speed lines|Impact frames|Screen tones|Action typography|Cel shading'}
}
for section, families in styles.items():
 for name,items in families.items():group('Styles and inspiration',section,name,items)
for name,items in {
'Short form':'Fact video|Vertical explainer|Countdown list|Before/after|Quote reel|Tutorial|Product tip|Social announcement|Animated meme|Quiz question',
'Long form':'Map documentary|Science explainer|Historical timeline|Technology review|Sports analysis|Financial explainer|Educational lesson|Interview graphics|Chapter sequence',
'Brand and product':'App launch|Feature demo|Product ad|Logo intro|Event opener|Pitch deck motion|Website hero loop|Onboarding tour|Changelog video|Store promo',
'Broadcast packages':'Lower thirds|Breaking news|Scoreboard|Weather segment|News ticker|Election map|Studio backdrop|Credits|Sponsor bumper'
}.items():group('Video formats and scenes','Reusable sequences',name,items)
for name,items in {
'Camera':'Pan|Tilt|Dolly|Truck|Crane|Orbit|Handheld|Follow target|Rack focus|Isometric|Orthographic|Perspective|Depth parallax',
'Lighting':'Studio softbox|Three point|Rim light|HDRI|Neon|Daylight|Golden hour|Volumetric|Caustics|Shadow animation',
'Motion mechanics':'Easing curves|Spring settings|Stagger|Anticipation|Overshoot|Follow through|Loop continuity|Speed ramp|Beat synchronization|Motion path|Anchor points|Shared element',
'Delivery':'16:9 landscape|9:16 portrait|1:1 square|4:5 social|Transparent WebM|Alpha ProRes|H.264 MP4|GIF|Lottie JSON|SVG animation|Rive file|Reduced motion|Safe areas|Captions|Audio loudness|Frame rate'
}.items():group('Production building blocks','Reusable techniques',name,items)
for name,items in {
'2D and UI':'Remotion composition|React component|CSS keyframes|Web Animations API|SVG paths|Canvas scene|GSAP timeline|Motion component|Lottie player|Rive runtime',
'3D and maps':'Three.js scene|React Three Fiber|Blender project|MapLibre scene|D3 geography|Deck.gl layer|Globe component|GeoJSON pipeline',
'Automation':'Deterministic frame clock|Seeded randomness|Editable parameter schema|Asset preloading|Font loading|Audio timing|Preview contact sheet|Render script|Manifest search|Dependency lockfile'
}.items():group('Code recipes and integrations','Implementation catalog',name,items)
group('Animations','Objects, nature and characters','Thought bubbles and icons','Thought bubble appear|Thought bubble morph|Speech bubble pop|Dream cloud|Idea burst|Question mark bounce|Exclamation pop|Icon draw|Icon morph|Icon stroke loop|Mood icon change|Sound wave pulse')
# Color treatments are collection targets; named references require real examples later.
for name,items in {
'Breaking Bad-inspired':'Desert yellow and amber|Green fluorescent interiors|Bleached sunlit exteriors|Deep shadow contrast|Warm/cool scene contrast|Reference frame palette study',
'Better Call Saul-inspired':'Warm desert daylight|Clean office neutrals|Saturated accent colors|Cool night interiors|Black-and-white timeline look|Reference frame palette study',
'Stranger Things-inspired':'Neon red and blue|Warm retro interiors|Cold supernatural atmosphere|Deep night shadows|1980s film finish|Reference frame palette study',
'Euphoria-inspired':'Purple and cyan lighting|Pink neon highlights|Dreamy glow|Soft highlight bloom|Bold skin-safe color separation|Reference frame palette study',
'Mr. Robot-inspired':'Cool green cast|Muted urban palette|Low-key shadows|Pale fluorescent look|Restrained saturation|Reference frame palette study',
'Peaky Blinders-inspired':'Muted industrial palette|Cool steel shadows|Warm practical lights|Smoky contrast|Period film finish|Reference frame palette study',
'Dark-inspired':'Muted forest greens|Cold blue-gray palette|Soft overcast contrast|Dark interior treatment|Restrained warm accents|Reference frame palette study',
'The Last of Us-inspired':'Muted natural greens|Warm daylight highlights|Weathered earth tones|Soft desaturated shadows|Overcast atmosphere|Reference frame palette study',
'Succession-inspired':'Natural corporate neutrals|Cool interior palette|Restrained saturation|Warm evening interiors|Subtle film contrast|Reference frame palette study',
'Wednesday-inspired':'Cool gothic palette|Deep black separation|Muted purples|Pale highlights|Selective color accents|Reference frame palette study',
'Game of Thrones-inspired':'Cold northern palette|Warm firelit interiors|Desaturated battlefield|Golden southern palette|Night scene contrast|Reference frame palette study',
'The Bear-inspired':'Natural kitchen whites|Warm practical lights|Cool stainless steel|Documentary contrast|Night street palette|Reference frame palette study'
}.items():group('Color grading and looks','Series-inspired looks',name,items)
for name,items in {
'Film and genre references':'The Matrix-inspired green|Blade Runner-inspired neon|Dune-inspired desert|Mad Max-inspired orange/cyan|Wes Anderson-inspired pastel|Noir monochrome|Neo-noir night|Western earth tones|Horror cold shadows|Romantic warm glow|Documentary natural color|Vintage home movie',
'Everyday filter families':'Warm|Cool|Neutral clean|High contrast|Low contrast|Faded blacks|Matte finish|Desaturated|Vibrant|Pastel|Sepia|Black and white|Duotone|Teal and orange|Bleach bypass|Cross processed|Infrared-inspired|Night vision-inspired|Thermal-inspired',
'Color controls':'Exposure|White balance|Tint|Contrast curve|Lift gamma gain|Shadows midtones highlights|Saturation|Vibrance|Hue rotation|Selective color|Skin tone protection|Highlight rolloff|Shadow tint|Highlight tint|Color matching|Shot matching',
'LUTs and delivery':'Creative LUT reference|Technical conversion LUT|Log to Rec.709 transform|Cube LUT file|LUT intensity control|Before/after comparison|Input color space record|Output color space record|Exposure test chart|Skin tone test frames|Day/night variants|Mobile preview check',
'Film and finishing looks':'Fine film grain|Coarse film grain|Warm halation|Soft bloom|Vintage lens softness|Faded print|Film print contrast|Analog color drift|Highlight clipping reference|Split toning|Silver-rich monochrome|Color isolation'
}.items():group('Color grading and looks','Filter families and controls',name,items)
for name,items in {
'Paper and print':'Clean paper|Recycled paper|Kraft paper|Newspaper|Notebook paper|Graph paper|Wrinkled paper|Torn paper edges|Cardboard|Old book paper|Photocopy|Risograph|Offset print|Halftone dots|Ink bleed|Print misregistration',
'Film and analog':'Fine grain|Coarse grain|Dust specks|Film scratches|Gate weave|Film burn|Light leak|VHS noise|CRT scanlines|Tape tracking|Super 8 frame|35mm frame|Film perforations|Projected film flicker',
'Natural surfaces':'Wood grain|Tree bark|Stone|Marble|Granite|Sand|Soil|Grass|Leaves|Water surface|Ice|Snow|Clouds|Leather|Animal fur',
'Built materials':'Brushed metal|Polished chrome|Rusted metal|Scratched steel|Concrete|Cracked concrete|Brick|Plaster|Ceramic|Glass|Frosted glass|Plastic|Rubber|Carbon fiber|Asphalt',
'Fabric and craft':'Cotton|Linen|Denim|Canvas|Velvet|Silk|Knitted fabric|Woven fabric|Felt|Embroidery|Stitching|Watercolor paper|Pencil shading|Charcoal|Crayon|Paint strokes',
'Digital and abstract':'Noise field|Dither|Pixel grid|Dot matrix|Wire mesh|Holographic foil|Iridescence|Gradient mesh|Topographic lines|Voronoi cells|Fluid marbling|Fractal field|Moiré pattern|Circuit pattern|ASCII texture',
'Grunge and distressed':'Grunge overlay|Dirty lens|Smudges|Fingerprints|Scraped paint|Peeling paint|Water stains|Coffee stains|Burned edges|Cracked ink|Weathered signage|Torn poster layers'
}.items():group('Textures','Surface library',name,items)
for name,items in {
'Animated texture loops':'Drifting grain|Boiling paper|Moving dust|Scratching film|Flickering scanlines|Scrolling noise|Flowing ink|Rippling water|Shimmering foil|Animated halftone|Crawling dither|Hand-drawn line boil',
'Overlay and compositing':'Transparent overlay|Screen blend variant|Multiply blend variant|Soft light variant|Opacity control|Texture mask|Luma matte|Displacement map|Edge wear mask|Animated reveal mask',
'3D texture maps':'Base color / albedo|Roughness|Metalness|Normal map|Bump map|Height / displacement|Ambient occlusion|Emission|Opacity|Packed ORM map',
'File and quality variants':'Seamless tile|Non-tiling plate|Portrait overlay|Landscape overlay|Square tile|2K texture|4K texture|8K source|PNG transparency|EXR linear map|Color space metadata|Physical scale record|Loop seam review|Source and license record'
}.items():group('Textures','Motion, maps and delivery',name,items)

# Media and editorial collections: targets only, with provenance recorded when collected.
for name,items in {
'People and everyday life':'Walking crowd|Commuting|Studying|Reading|Writing notes|Cooking|Eating|Shopping|Conversation|Waiting|Sleeping|Celebrating|Working at a desk|Family moment|Hands using a phone|Hands typing|Hands exchanging an object',
'Technology and AI':'Phone closeup|Laptop typing|Server racks|Data center exterior|Circuit board macro|Robot arm|Factory automation|VR headset use|Game controller use|App interaction recording|AI chat screen capture|Coding screen|Camera equipment|Satellite dish|Computer repair',
'Business and money':'Office teamwork|Meeting room|Presentation|Small business storefront|Warehouse packing|Delivery|Cash counting|Card payment|ATM use|Stock exchange exterior|Financial dashboard recording|Contract signing|Job interview|Construction progress',
'Cities and transport':'City establishing shot|Street crossing|Traffic timelapse|Night traffic|Subway platform|Train arrival|Train window|Plane takeoff|Airport terminal|Port cranes|Cargo ship|Highway aerial|Walking POV|Driving POV|Cycling POV|Road sign insert',
'Nature and geography':'Mountain aerial|Forest canopy|River aerial|Ocean coastline|Waves closeup|Desert dunes|Rain on window|Storm clouds|Sunrise|Sunset|Night sky|Flower macro|Wildlife|Underwater|Snow landscape|Volcano landscape',
'Science and education':'Classroom|Laboratory|Microscope|Chemical reaction|Physics demonstration|Whiteboard writing|Library shelves|Telescope|Hospital corridor|Medical equipment|Renewable energy|Space launch|Astronaut archive pointer',
'Sport and entertainment':'Football stadium|Ball closeup|Training drills|Running|Gym workout|Crowd cheering|Concert crowd|Musician hands|Headphone listening|Gaming setup|Theater seats|Backstage preparation',
'Abstract and metaphorical':'Clock passing time|Hourglass|Falling dominoes|Puzzle pieces|Maze|Empty chair|Opening door|Bridge crossing|Crossroads|Spinning coin|Chess move|Growing plant|Burning match|Water drop|Stacking blocks'
}.items():group('B-roll','Subject collections',name,items)
for name,items in {
'Shot types':'Wide establishing shot|Medium action shot|Closeup insert|Extreme macro|Over-the-shoulder|POV shot|Top-down shot|Low-angle shot|High-angle shot|Drone reveal|Tracking shot|Locked-off shot|Slow motion|Timelapse|Hyperlapse|Seamless loop',
'Editorial purpose':'Location setup|Time passing|Process demonstration|Evidence illustration|Visual metaphor|Transition bridge|Narration coverage|Detail emphasis|Scale comparison|Atmosphere bed|Problem example|Outcome example',
'Collection metadata':'Source and creator record|Usage rights record|Model release record|Property release record|Capture date and location|Resolution and frame rate|Duration and usable range|Camera movement tags|Orientation variants|Original audio record|Clean plate variant|Transcript or shot description'
}.items():group('B-roll','Shot selection and delivery',name,items)
for name,items in {
'Reaction moods':'Confusion|Disbelief|Shock|Suspicion|Realization|Awkward silence|Embarrassment|Frustration|Anger|Disappointment|Celebration|Relief|Approval|Disapproval|Panic|Sadness|Boredom|Anticipation|Smug confidence|Dramatic defeat',
'Familiar reaction references':'Confused math lady|Blinking white guy|Dramatic chipmunk|This is fine|Surprised Pikachu|Disappointed cricket fan|Facepalm reaction|Slow clap reaction|Spit take reaction|Record scratch freeze|Wait a minute reaction|Mind blown reaction|Confused Travolta|Shocked crowd|Happy dance reaction',
'Comedic actions':'Double take|Slow turn|Zoom into face|Walking away|Running away|Falling over|Chair spin|Head shake|Nervous glance|Thumbs up|Suspicious squint|Mic drop|Desk slam|Celebration jump|Looking into camera|Dramatic entrance',
'Animals and characters':'Confused dog|Side-eye dog|Surprised cat|Keyboard cat reference|Dancing animal|Judgmental bird|Goofy walk|Cartoon panic|Cartoon impact|Stickman reaction|Mascot reaction|Video game NPC reaction',
'Editing formats':'Full-frame cutaway|Corner reaction insert|Green-screen cutout|Transparent reaction loop|Freeze-frame punchline|Captioned reaction|Silent reaction|Reaction with original audio|Sound-only punchline pointer|Split-screen comparison|Vertical crop|Looping GIF reference|Before/after punchline',
'Comedic timing':'Setup pause|Anticipation hold|Hard cut punchline|Delayed reaction|Rapid repeat|Escalating repeat|Smash zoom|Deadpan hold|Awkward extended hold|Fake-out reveal|Callback insert|Cut on sound',
'Context and source notes':'Original source link|Original context summary|Creator and rights record|Timestamp and usable segment|Reaction meaning|Suggested edit use|Audio transcript|Language and translation|Clean language variant|Crop-safe area|Caption-safe area|Attribution requirements'
}.items():group('Meme clips and reactions','Reaction library',name,items)
for name,items in {
'Historical material':'Historic street footage|Historic city photograph|Public speech recording|Newsreel reference|Historic map|Old newspaper page|Scanned letter|Diary page|Government report|Patent drawing|Scientific illustration|Historic advertisement|Election material|Museum object photograph',
'Evidence and documents':'Research paper extract|Book excerpt reference|Official statistics table|Court document pointer|Company filing pointer|Press release|Public statement|Verified quotation|Original interview pointer|Web page capture|Document comparison|Source citation card',
'Editorial source organization':'Archive institution record|Original publication date|Event date|Author and creator record|Provenance chain|Source URL|Archive identifier|Rights statement|Caption and context|Transcript pointer|Translation note|Restoration history'
}.items():group('Archival media and documents','Evidence collections',name,items)
for name,items in {
'Portraits and people':'Headshot|Full-body portrait|Side profile|Expressive portrait|Hands detail|Crowd image|Athlete portrait|Musician portrait|Scientist portrait|Historical figure reference|Silhouette|Background-removed person',
'Products and places':'Product packshot|Product detail|Device screen image|Packaging|Building exterior|Room interior|City skyline|Landmark|Landscape|Food photograph|Vehicle|Aerial image',
'Cutouts and editorial assets':'Transparent object cutout|Hair-edge portrait cutout|Paper-edged photo cutout|Sticker-style cutout|Shadow-only layer|Foreground isolation|Background isolation|Depth-separated photo|Object mask|Face-safe crop|Caption-safe crop|Portrait/landscape crop variants',
'Photo animation preparation':'2.5D parallax layers|Depth map|Inpainted background plate|Subject anchor points|Ken Burns crop path|Focus region|Photo carousel sequence|Contact sheet|Source and license record|Image caption and alt text'
}.items():group('Photography and cutouts','Still image collections',name,items)
for name,items in {
'Practical visual elements':'Smoke plume|Fog layer|Fire element|Spark shower|Ember drift|Water splash|Rain layer|Snow layer|Dust hit|Debris burst|Glass fragments|Ink in water|Light beam|Lens flare element',
'Keying and masks':'Green-screen reference|Blue-screen reference|Garbage matte|Chroma key settings|Spill suppression|Hair edge refinement|Rotoscope mask|Luma key|Depth matte|Object occlusion mask|Holdout matte|Edge feather control',
'Tracking and integration':'Point tracking reference|Planar tracking reference|Camera solve reference|Phone screen replacement|Laptop screen replacement|Billboard replacement|Text attached to surface|Moving object label|Perspective corner pin|Shadow matching|Light wrap|Reflection matching',
'Composite building blocks':'Foreground plate|Background plate|Clean plate|Shadow pass|Reflection pass|Depth pass|Motion vector pass|Alpha premultiplication record|Blend mode comparison|Color match pass|Grain match pass|Before/after composite'
}.items():group('VFX and compositing','Compositing library',name,items)
for name,items in {
'Color systems':'Monochrome palette|Two-color palette|Three-color palette|Pastel palette|Neon palette|Earth-tone palette|Editorial palette|Technology palette|Sports palette|Warm/cool contrast|Category color mapping|Accessible contrast pair',
'Layout recipes':'Centered hero|Editorial column|Split-screen|Asymmetric composition|Bento grid|Card grid|Photo collage|Timeline layout|Comparison layout|Map plus sidebar|Chart plus annotation|Full-screen quote|Poster layout|Device showcase',
'Brand ingredients':'Logo variants|Logo clear space|Brand palette|Typography pairing|Icon style guide|Corner radius system|Stroke width system|Shadow system|Spacing scale|Background treatment|Motion timing tokens|Sound identity',
'Composition guides':'Rule of thirds|Centered symmetry|Golden ratio guide|Baseline grid|Eight-point spacing grid|Portrait safe areas|Landscape safe areas|Caption exclusion area|Logo exclusion area|Visual hierarchy check|Foreground/background separation|Negative space planning'
}.items():group('Palettes and design systems','Reusable design recipes',name,items)
for name,items in {
'Story beats':'Curiosity hook|Question opener|Claim reveal|Context setup|Problem setup|Evidence reveal|Mechanism explanation|Counterexample|Comparison|Escalation|Twist|Payoff|Recap|Call to action',
'Editing patterns':'Narration-led montage|Beat-led montage|J-cut|L-cut|Match on action|Cutaway insert|Reaction insert|Parallel editing|Split-screen comparison|Time compression|Time expansion|Freeze and annotate|Zoom and explain|Visual callback',
'Sequence planning':'Script-to-shot breakdown|Storyboard panels|Shot list|Animatic|Narration cue sheet|Music cue sheet|Sound cue sheet|Scene duration plan|Transition plan|Reusable scene graph|Source checklist|Render review sheet',
'Pacing references':'Fast educational pacing|Calm documentary pacing|Comedy pause timing|Product reveal pacing|Suspense buildup|Impact beat|Breathing room|Information-dense sequence|Mobile short pacing|Looping ending'
}.items():group('Storytelling and editing','Editorial recipes',name,items)
for name,items in {
'Caption styles':'Clean subtitles|Word-highlight captions|Karaoke captions|Speaker-labeled captions|Two-line subtitles|Bilingual captions|Vertical short captions|Transcript overlay|Quote emphasis|Sound description captions',
'Localization':'English version|Spanish version|Translation glossary|Pronunciation notes|Subtitle timing adaptation|Text expansion layout|Right-to-left layout|Locale number formats|Locale date formats|Culturally specific reference notes',
'Accessibility and delivery':'Readable contrast|Minimum type size guide|Reduced motion variant|Flash and strobe review|Color-independent labels|Safe caption position|Dialogue intelligibility|Music ducking|Descriptive transcript|Alt text for stills|SRT file|WebVTT file|Burned-in captions|Clean video without captions'
}.items():group('Captions and localization','Text and accessibility',name,items)
for name,items in {
'Voice direction':'Calm explainer|Energetic explainer|Documentary narrator|News presenter|Conversational read|Dramatic read|Deadpan comedy|Warm instructional read|Character reaction|Whispered line',
'Voice production':'Script with emphasis marks|Pronunciation guide|Spanish pronunciation sample|English pronunciation sample|Pacing reference|Breath placement|Pause markers|Pickup line record|Clean narration take|Room tone|Noise removal settings|De-essing settings|Loudness target record|Music ducking envelope',
'Alignment and assets':'Sentence timing markers|Word timing markers|Phoneme timing markers|Caption alignment|Character lip-sync reference|Voice consent and usage record|Speaker identity record|Language and accent tags|Raw take pointer|Edited take pointer'
}.items():group('Voiceover and narration','Narration library',name,items)

# Generate stable IDs; do not create speculative combinations across every subject.
def slug(s):return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
count=0
def node(label,value,path):
 global count
 current=path+[label]; ident='/'.join(map(slug,current))
 if isinstance(value,dict):return {'id':ident,'name':label,'children':[node(k,v,current) for k,v in value.items()]}
 if isinstance(value,list):return {'id':ident,'name':label,'children':[node(k,None,current) for k in value]}
 count+=1
 return {'id':ident,'name':label,'status':'planned','priority':'normal','tags':[slug(p) for p in path[-2:]],'notes':'','references':[],'preview':None,'code':None,'files':[],'license':None,'variants':[]}
catalog={'version':1,'title':'Motion Atlas','description':'A growing collection of motion references, assets and reusable implementations.','categories':[node(k,v,[]) for k,v in T.items()]}
(ROOT/'dist/catalog.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
(ROOT/'docs/CATALOG.md').write_text('# Collection checklist\n\nGenerated from scripts/build_catalog.py. All entries begin as planned.\n\n'+'\n'.join('## '+c+'\n\n'+'\n'.join('### '+s+'\n\n'+'\n'.join('**'+n+'**\n\n'+'\n'.join('- [ ] '+i for i in items)+'\n' for n,items in families.items()) for s,families in sections.items()) for c,sections in T.items()))
print(f'{len(T)} categories; {count} specific collection entries')
