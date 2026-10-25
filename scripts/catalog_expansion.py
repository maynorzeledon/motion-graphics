"""Additional collection targets and presentation hierarchy. No creator analyses are pre-filled."""
CREATORS = {
'MrBeast':('Challenge and spectacle','Immediate challenge premise|Rules and stakes|Outcome preview','Escalating obstacles|Contestant progress|Midpoint rule change','Winner reveal|Emotional result|Final consequence'),
'Zack D. Films':('Short factual stories','Unusual factual question|Scenario setup|Immediate visual problem','Cause-and-effect chain|Mechanism explanation|Complication or exception','Surprising consequence|Answer the opening question|Compact final fact'),
'Vsauce':('Curiosity and science','Everyday question|Counterintuitive claim|Thought experiment','Connected question chain|Analogy to abstract idea|Detour that returns to premise','Conceptual reframe|Return to opening question|Reflective ending'),
'grantbeans':('Absurdist sketch comedy','Ordinary situation|Casual character introduction|Unexpected interruption','Reality shift|Escalating misunderstanding|New context changes prior scene','Circular ending|Abrupt punchline|Earlier detail becomes payoff'),
'jercho1':('Absurdist sketch comedy','Everyday social premise|Character tension|Unexpected response','Deadpan escalation|Surreal consequence|Character logic reversal','Visual punchline|Recontextualized setup|Loop back to opening'),
'Vine — platform format':('Micro-sketch formats','Instantly readable situation|One-line premise|Visual setup','Single comic turn|Fast character switch|Compressed escalation','Hard-cut punchline|Six-second loop|Reaction as final beat'),
'Mark Rober':('Experiments and engineering','Engineering challenge|Demonstration teaser|Personal reason to care','Prototype failure|Iteration and testing|Explain the mechanism','Final experiment|Measured result|Human payoff'),
'Veritasium':('Curiosity and science','Common intuition|Question with a trap|Counterintuitive result','Test the misconception|Evidence reveal|Deeper explanation','Revised mental model|Experiment resolution|Open scientific question'),
'Kurzgesagt':('Animated explanation','Big question|Scale-setting scenario|Consequential premise','Layered explanation|Competing possibilities|Scale escalation','Qualified answer|Bigger-picture implication|Reflection'),
'Johnny Harris':('Documentary and investigation','Location-linked mystery|Personal discovery|Claim to investigate','Historical context|Evidence trail|Map-led explanation','Answer the mystery|Present-day consequence|Return to location'),
'Vox':('Documentary and investigation','Observable puzzle|News-linked question|Concrete example','Historical explanation|Data and evidence|Expert context','Explanatory conclusion|Wider implication|Return to example'),
'LEMMiNO':('Documentary and investigation','Unresolved mystery|Case context|Key question','Chronological evidence|Competing hypotheses|Contradictory evidence','Known versus unknown|Reasoned conclusion|Unresolved thread'),
'fern':('Documentary and investigation','Event or mystery|Character introduction|High-stakes question','Causal timeline|Perspective change|Reconstruction and evidence','Consequences|Case resolution|Lingering question'),
'3Blue1Brown':('Mathematics and visual intuition','Visual puzzle|Intuition gap|Simple example','Geometric model|Build toward formalism|Transform the representation','Mathematical insight|Connect to original puzzle|Generalize the idea'),
'SmarterEveryDay':('Experiments and engineering','Personal curiosity|Physical demonstration|Question from observation','Field experiment|Slow-motion evidence|Expert explanation','Changed intuition|Repeat the demonstration|Personal reflection'),
'Tom Scott':('Concise explanation','Distinctive place or object|Surprising constraint|Direct question','Practical mechanism|Relevant context|Exception to the rule','Concise explanation|Location callback|Final implication'),
'CGP Grey':('Animated explanation','Simple system question|Common assumption|Definition problem','Rules and incentives|Edge cases|Consequences of the system','System-level insight|Qualified conclusion|Memorable analogy'),
'Wendover Productions':('Systems and logistics','Logistical puzzle|Cost or route question|Concrete business example','Constraints and incentives|Network explanation|Trade-off comparison','System outcome|Economic consequence|Return to example'),
'Half as Interesting':('Concise explanation','Odd fact|Specific question|Unexpected historical detail','Compact context|Causal explanation|Comic aside placement','Answer|Final odd detail|Callback joke'),
'Kento Bento':('Documentary and investigation','High-stakes incident|Character and location|Unanswered question','Chronological suspense|Complication|Reveal withheld information','Event outcome|Reinterpretation|Consequences'),
'Ryan Trahan':('Personal challenge and journey','Personal constraint|Journey goal|Rules of the challenge','Daily progress|Setback and recovery|Unexpected encounter','Complete the goal|Human connection|Reflect on journey'),
'Yes Theory':('Personal challenge and journey','Uncomfortable challenge|Human connection premise|Personal fear','Commit to experience|Social uncertainty|Trust and discovery','Shared experience|Personal change|Reflective takeaway'),
'Casey Neistat':('Personal challenge and journey','Personal problem|Day-specific goal|Visual cold open','Journey through obstacles|Observation and reflection|Small story within the day','Personal resolution|Callback|Closing reflection'),
'Airrack':('Challenge and spectacle','Large challenge|Unusual mission|Clear external goal','Escalation|Logistical obstacle|Team response','Attempt outcome|Surprise reveal|Final consequence'),
'MKBHD':('Technology and reviews','Product question|First impression|Key trade-off','Experience-led sections|Comparison|Evidence for verdict','Who it is for|Qualified verdict|Return to main question'),
'Mrwhosetheboss':('Technology and reviews','Comparison promise|Unusual device question|Clear test premise','Ranked tests|Unexpected result|Escalating comparison','Final ranking|Buying context|Overall insight'),
'Drew Gooden':('Commentary and comedy','Specific observation|Comedic thesis|Example clip context','Build the argument|Contrast examples|Running joke progression','Thesis payoff|Callback|Personal conclusion'),
'Danny Gonzalez':('Commentary and comedy','Unusual media example|Question or premise|Comedic reaction','Pattern of examples|Escalation|Sketch interruption','Callback|Absurd conclusion|Resolve the premise'),
'Kurtis Conner':('Commentary and comedy','Cultural observation|Specific example|Comedic question','Example analysis|Running bit|Absurd comparison','Final comic verdict|Callback|Thesis restatement'),
'Ryan Higa / nigahiga':('Sketch and visual comedy','Wordplay premise|Genre parody setup|Character misunderstanding','Literal interpretation|Escalating visual joke|Recurring comic rule','Punchline reversal|Callback|Parody resolution'),
'Daniel Thrasher':('Sketch and visual comedy','Musical or social premise|Character conflict|Unexpected ability','Escalating performance|Role reversal|Absurd rule development','Musical payoff|Twist|Final reaction'),
'CalebCity':('Sketch and visual comedy','Recognizable trope|Character rule|Immediate conflict','Literal consequence|Rapid escalation|Logic of the world','Final contradiction|Hard-cut payoff|Last reaction'),
'LongBeachGriffy':('Sketch and visual comedy','Social situation|Exaggerated character premise|Immediate tension','Escalating response|Character contrast|Unexpected commitment','Absurd conclusion|Reversal|Hard cut'),
'XpressTV':('Lists and curiosity','Curiosity promise|Unexpected fact teaser|List framing','Fact-to-fact progression|Visual evidence pairing|Mini-story inside a fact','Strong final item|Question to audience|Closing callback'),
'Jaiden Animations':('Personal animated stories','Personal experience|Relatable problem|Comic premise','Character-driven events|Reflection mixed with action|Emotional complication','Personal lesson|Comic callback|Emotional resolution'),
'TheOdd1sOut':('Personal animated stories','Relatable observation|Childhood premise|Personal anecdote','Escalating examples|Animated cutaway|Character contrast','Opinion payoff|Anecdote resolution|Callback')
}
STYLE_CREATORS={
'Zack D. Films':'3D scene blocking|Cutaway anatomy study|Camera move study|Object-scale staging|Narration-synced action|On-screen emphasis|Lighting and materials study',
'Vsauce':'Presenter framing|Object demonstration insert|Scientific image treatment|Question text layout|Sound-led transition study|Cutaway image pacing|Simple explanatory graphics',
'MrBeast':'Large emphasis captions|Progress overlays|Challenge timers|Score and stakes graphics|Map inserts|Reaction punch-ins|High-energy montage study',
'grantbeans':'Casual phone framing|Deadpan performance framing|Unexpected visual insert|Abrupt location change|Surreal continuity edit|Hard-cut reaction|Loop transition study',
'jercho1':'Sketch character framing|Ordinary-to-surreal visual change|Reaction closeup|Abrupt cut treatment|Character blocking|Visual punchline staging|Continuity mismatch study',
'Mark Rober':'Experiment overlays|Prototype labels|Slow-motion insert|Engineering diagram|Measurement graphics|Test comparison|Result reveal graphics',
'Tom Scott':'Location presenter framing|Practical demonstration insert|Simple labels|Clean subtitle treatment|Concise cutaway sequence|On-location sound bed',
'CGP Grey':'Simple character diagrams|Flat vector symbols|System flow graphics|Map simplification|Shape-based transitions|Diagram color roles',
'Wendover Productions':'Transport map graphics|Logistics diagrams|Stock footage integration|Route labels|Data graphic overlays|Documentary chapter cards',
'Half as Interesting':'Fast visual inserts|Concise labels|Diagram simplification|Comic visual aside|Map insert treatment|Short explanatory montage',
'MKBHD':'Product macro|Studio product lighting|Clean specification cards|Device camera moves|Desk composition|Comparison framing',
'Mrwhosetheboss':'Comparison layouts|Device lineup|Score graphics|Product transition|Reaction framing|Test evidence insert',
'Casey Neistat':'Handmade titles|Time-lapse inserts|POV montage|Practical camera moves|Hand-drawn diagrams|Everyday object transitions',
'Ryan Trahan':'Journey map insert|Day counter|Casual handheld montage|Challenge overlay|Reaction closeup|Progress recap treatment',
'Daniel Thrasher':'Piano performance framing|Character shot reversal|Musical beat cut|Reaction punch-in|Deadpan hold|Visual performance gag',
'CalebCity':'Character shot reversal|Impact cut|Reaction hold|Speed emphasis|Minimal caption treatment|Hard-cut punchline',
'Jaiden Animations':'Expressive 2D poses|Hand-drawn scene staging|Limited animation timing|Illustrated cutaways|Character mouth shapes|Narrated action sync',
'TheOdd1sOut':'Simple character silhouettes|Flat scene composition|Expressive pose swaps|Textured illustration|Visual exaggeration|Comic cutaway staging',
'XpressTV':'Fact title cards|Numbered item transitions|Photo and footage montage|Object emphasis graphics|Caption hierarchy|Fact comparison layouts'
}
def extend(group):
 group('Storytelling and editing','Comedy formats','Literal jokes',{
  'Idioms acted out':['Break the ice → break a block of ice','Hold your horses → physically hold toy horses','On the fence → sit on an actual fence','Spill the beans → spill a bag of beans','A piece of cake → reveal an actual piece of cake'],
  'Metaphors made physical':['Time flies → a clock grows wings','Lost my train of thought → a toy train disappears','Food for thought → serve a brain-shaped snack','Heavy conversation → speech bubbles become heavy','Running out of time → a clock runs away'],
  'Ambiguous words and requests':['Give me a hand → pass over a mannequin hand','Make it snappy → answer with finger snaps','Take a seat → carry a chair away','Draw the curtains → sketch a pair of curtains','Watch your step → point a camera at a staircase'],
  'Story construction':['Ordinary conversation setup','Hide the literal interpretation until the reveal','Reveal the physical meaning','Character treats the literal result as normal','Escalate the same literal rule','Callback to an earlier expression'],
  'Punchline delivery':['Visual-only literal reveal','Dialogue plus literal prop reveal','Deadpan literal answer','Delayed realization','Second meaning revealed by a wider shot'],
  'Reference studies':['Video and transcript reference','Timecoded visual joke breakdown','Expression → literal meaning → visual payoff','Reusable literal-joke script blueprint','Original literal-joke ideas']
 })
 group('Styles and inspiration','Comedy editing styles','Literal-joke visual treatment','Prop reveal framing|Wide-shot meaning reveal|Literal text-to-object transformation|Deadpan reaction hold|Match cut from phrase to object|On-screen wordplay emphasis')
 for creator,(genre,hook,development,ending) in CREATORS.items():
  # Four separate folders per creator; observations stay empty until real examples arrive.
  group('Storytelling and editing','Creator studies — '+genre,creator, {'Reference library':['Video, script and visual study 01','Video, script and visual study 02','Reusable story blueprint'],'Hooks and premise':hook.split('|'),'Progression and escalation':development.split('|'),'Payoff and ending':ending.split('|'),'Analysis worksheets':['Timecoded script','Visual beat sheet','Open loops and callbacks','Narrator-to-visual relationship']})
 for creator,items in STYLE_CREATORS.items():group('Styles and inspiration','Creator editing studies',creator+' — visual editing',items)
 families={
 'Explainer styles':{
 'Flat vector explainer':'Geometric characters|Icon-led scenes|Flat scene transitions|Two-color diagram|Layered vector landscape|Narrated object action',
 '3D mechanism explainer':'Exploded assembly|Internal cutaway|Transparent shell|Step-by-step mechanism|Scale comparison|Object transformation',
 'Whiteboard explainer':'Hand-drawn line reveal|Marker labels|Erase and redraw|Doodle connectors|Sketch scene build|Handwriting titles',
 'Editorial collage explainer':'Photo cutouts|Document highlights|Newspaper layers|Map plus photo|Paper texture|Source label hierarchy',
 'UI and software explainer':'Cursor choreography|Screen focus zoom|Step highlight|Window stacking|Input-to-result sequence|Feature callouts',
 'Minimal diagram explainer':'Line drawing|Node systems|Symbolic objects|Negative-space layout|Restrained typography|Single accent color',
 'Classroom and chalkboard':'Chalk texture|Equation build|Handwritten labels|Grid background|Diagram annotations|Worked-example highlights',
 'Medical and science visualization':'Anatomy cutaway|Cell-scale scene|Molecule view|Process arrows|Transparent layers|Scale labels'},
 'Lyrics and song videos':{
 'Classic lyric video':'Centered lyric lines|Line-by-line fades|Verse/chorus changes|Simple scenic background|Readable lyric contrast|Intro and outro credits',
 'Karaoke lyrics':'Syllable highlight|Word timing|Bouncing ball marker|Upcoming line preview|Duet color roles|Instrumental gap treatment',
 'Kinetic typography lyrics':'Word pop on beat|Letter stretch|Text-path movement|Phrase composition|Chorus scale change|Beat-linked transitions',
 'Cinematic lyric video':'Landscape footage|Slow camera drift|Film texture|Serif lyric layout|Soft crossfades|Scene-linked lyric placement',
 'Handwritten lyrics':'Notebook handwriting|Ink reveal|Paper collage|Doodle accents|Handwritten chorus|Scratched-out word treatment',
 'Music visualizer':'Waveform|Spectrum bars|Circular spectrum|Particle response|Beat pulse|Frequency-reactive background',
 'Album-art loop':'Cover art parallax|Spinning record|Ambient particle layer|Subtle camera motion|Looping light|Track title treatment',
 'Vertical social song edit':'Portrait lyric-safe area|Hook lyric emphasis|Beat cuts|Phone-friendly type|Short looping segment|Caption spacing',
 'Genre-inspired lyric treatments':'Pop color blocks|Rock distressed type|Rap bold captions|Indie film collage|Electronic neon type|Acoustic handwritten layout'},
 'Additional editing families':{
 'Sports and hype':'Freeze-frame athlete|Score overlays|Speed ramp study|Impact typography|Replay split-screen|Crowd montage',
 'Gaming and streams':'HUD-inspired overlays|Kill-feed treatment|Facecam layout|Chat overlay|Achievement pop|Highlight replay',
 'Travel and lifestyle':'Postcard title|Destination labels|Film montage|Travel route overlay|Date stamp|Ambient scenic loop',
 'Food and recipe':'Ingredient cards|Top-down composition|Step labels|Measurement overlays|Texture macro|Before/after plate',
 'Fashion and beauty':'Editorial crop|Product swatch|Magazine typography|Texture closeup|Mirror composition|Runway cut rhythm',
 'True crime and investigation':'Evidence board|Case timeline|Document redaction|Location map|Archival photo treatment|Transcript emphasis',
 'History and archival':'Restored photo motion|Period typography|Historic map overlay|Timeline ribbon|Archival frame|Document zoom',
 'Finance and business':'Market ticker|Clean dashboards|Currency counters|Executive summary card|Bar comparison|Company timeline',
 'Podcast and interview':'Speaker layout|Quote highlights|Waveform strip|Chapter labels|Multi-camera crop|Audio-first B-roll sequence',
 'Stop motion and mixed media':'Paper cutout sequence|Clay frame cadence|Collage replacement|Handmade jitter|Object stop motion|Photo-to-doodle transition',
 'Retro internet and memes':'Old desktop UI|Low-resolution insert|Deliberate compression|Forum screenshot treatment|GIF loops|Early-web typography',
 'Cinematic and atmospheric':'Wide composition|Slow reveal|Lens texture|Deep shadow staging|Practical light accents|Quiet typography'}
 }
 for section,fams in families.items():
  for name,items in fams.items():group('Styles and inspiration',section,name,items)
 # Richer non-creator storytelling references.
 story={
 'Narrative structures':{
 'Curiosity and explanation':'Question → intuition → contradiction → answer|Mystery → clues → explanation|Small example → wider system|Thought experiment → consequence|Claim → evidence → qualification',
 'Challenges and journeys':'Goal → rules → attempts → result|Constraint → setback → adaptation|Before → process → after|Personal goal → social encounter → change|Competition → elimination → final outcome',
 'Comedy and short sketches':'Setup → escalation → punchline|Normal → strange → absurd|Literal interpretation of a phrase|Rule of three|Status reversal|Mistaken identity|Circular sketch|Deadpan anticlimax',
 'Documentary and argument':'Character → conflict → consequence|Chronological case|Parallel timelines|Investigation → competing explanations|Argument → counterargument → synthesis|Event → context → present-day impact'},
 'Script and visual analysis':{
 'Reference packets':'Original video|Transcript|Timecoded script|Shot-by-shot storyboard|Visual beat sheet|Audio cue map|Source notes|Story blueprint',
 'Hook analysis':'First image|First spoken line|Question opened|Information withheld|Viewer promise|Starting stakes|Context required',
 'Development analysis':'Scene objective|New information per beat|Causal links|Open loops|Re-hooks|Tension changes|Character motivation|Exposition placement',
 'Ending analysis':'Payoff resolves promise|Callback mapping|Emotional shift|Final image|Loop connection|Unanswered question|Last spoken line'},
 'Short-form formats':{
 'Vine-style micro-sketches':'Six-second setup/payoff study|One-location sketch|Two-character misunderstanding|Visual-only punchline|Looped ending|Abrupt final cut',
 'Reels and Shorts':'Immediate premise|Compact causal explanation|Miniature character arc|Fast escalation|Twist ending|Visual reset loop',
 'Absurdist and surreal comedy':'Ordinary-world setup|Unexplained reality shift|Character commits to strange logic|Context collapse|Unexpected character reveal|Impossible consequence|Straight-faced delivery|Recursive ending'}
 }
 for section,fams in story.items():
  for name,items in fams.items():group('Storytelling and editing',section,name,items)
 # Give every existing tab multiple substantive sections, not just a single wrapper folder.
 extra={
 'Animations':('Timing and interaction studies',{'Timing recipes':'Anticipation pose|Overshoot and settle|Follow-through delay|Stagger directions|Loop seam|Hold and release','Responsive variants':'Portrait layout|Landscape layout|Reduced motion|Touch interaction|Mouse interaction|Keyboard focus motion'}),
 'Maps and geography':('Scene recipes',{'Geography stories':'Country comparison|Border change timeline|Trade route explanation|City growth study|Terrain cross-section|Route with altitude','Reference packets':'Source map|Camera path|Layer manifest|Timecoded narration|Map legend|Boundary date record'}),
 '2D assets':('Reusable scene kits',{'Character kits':'Front and side poses|Expression sheet|Hand gestures|Mouth shapes|Layered source|Pose pivots','Scene kits':'Interior props|Street props|Desk objects|Science lab props|Nature foregrounds|Scale reference figures'}),
 '3D assets':('Scene and animation kits',{'Animation-ready kits':'Object pivots|Articulated joints|Named materials|Screen UVs|Camera targets|Animation clips','Lighting scenes':'Soft product studio|Dark rim-light stage|Outdoor daylight|Medical cutaway stage|Miniature scene|Transparent object setup'}),
 'Sound effects':('Sound design recipes',{'Layered moments':'Toggle click plus spring|Whoosh plus impact|Logo sound mark|Tension riser to silence|Comic pause and hit|Text pop variations','Clip preparation':'Dry version|Reverb version|Short tail|Long tail|Volume matched|Clean loop'}),
 'Music':('Editing and arrangement',{'Music-to-picture':'Downbeat map|Section marker sheet|Verse/chorus timing|Build to reveal|Quiet narration section|Loop-compatible edit','Mood transitions':'Curious to tense|Tense to triumphant|Playful to deadpan|Calm to urgent|Dreamy to energetic|Outro resolve'}),
 'Fonts and typography':('Screen typography systems',{'Video type kits':'Explainer titles|Lyric captions|Documentary lower thirds|Comedy emphasis|Product specs|Map labels','Type behavior':'Line breaking|Text overflow|Variable weight motion|Numeral alignment|Accent support|Caption-safe margins'}),
 'Transitions and effects':('Sequence-specific recipes',{'Continuity transitions':'Object match|Shape match|Color match|Movement match|Camera direction match|Audio-led scene change','Reference packets':'Before frame|After frame|Transition duration|Mask source|Motion curve|Sound cue'}),
 'Video formats and scenes':('Complete reference packages',{'Explainer packages':'Question-led explainer|Process tutorial|Myth correction|Comparison|List of facts|Mechanism short','Music packages':'Full lyric video|Karaoke video|Visualizer loop|Album-art loop|Vertical song edit|Live performance overlay'}),
 'Production building blocks':('Scene planning',{'Staging':'Camera blocking|Subject anchor|Layer depth|Eye trace|Visual focus|Occlusion plan','Review guides':'Narration coverage|Visual clarity|Frame bounds|Loop continuity|Audio sync|Caption readability'}),
 'Code recipes and integrations':('Reusable scene architecture',{'Story-driven systems':'Timecoded script parser|Storyboard manifest|Beat timeline|Narration cue hooks|Scene parameter registry|Reusable shot presets','Asset systems':'Media preload list|Font registry|Audio markers|Preview generator|Asset resolver|Dependency manifest'}),
 'Color grading and looks':('Matching and reference packets',{'Look studies':'Reference stills|Neutral source frame|Primary adjustment notes|Secondary adjustment notes|Skin-tone comparison|Before/after frames','Shot matching':'Daylight to daylight|Mixed interior lighting|Night sequence|Phone-to-camera match|Archive-to-new footage|Scene palette continuity'}),
 'Textures':('Application recipes',{'Texture placement':'Text fill|Background plate|Edge distress|Masked overlay|3D surface|Transition matte','Texture behavior':'Static finish|Frame-varying grain|Slow drift|Looping displacement|Light-responsive shimmer|Beat-linked texture pulse'}),
 'B-roll':('Story coverage kits',{'Narration coverage':'Literal illustration|Contrast to narration|Metaphorical insert|Setting context|Process detail|Reaction coverage','Sequence building':'Wide-medium-close sequence|Action match|Three-shot process|Location transition|Time-passing montage|Revealing detail'}),
 'Meme clips and reactions':('Comedy reference packets',{'Reaction analysis':'Trigger line|Reaction onset|Hold duration|Punchline timestamp|Original context|Reusable meaning','Scene pairings':'Confident claim → failure|Serious explanation → absurd insert|Reveal → disbelief|Setup → awkward silence|Small win → huge celebration|Expectation → reversal'}),
 'Archival media and documents':('Visual storytelling with evidence',{'Document treatments':'Highlight key passage|Reveal a date|Compare two versions|Trace signature|Show publication context|Timecoded citation','Archive sequences':'Event timeline|Location then and now|Person profile|Historical claim and source|Photo-to-map bridge|Original context montage'}),
 'Photography and cutouts':('Photo-led scene recipes',{'Animated compositions':'Portrait quote card|Photo plus timeline|Layered parallax|Collage reveal|Product lineup|Location comparison','Preparation checks':'Subject mask|Clean background|Image resolution|Cropping options|Light direction|Depth separation'}),
 'VFX and compositing':('Shot-based recipes',{'Explainer composites':'Transparent body cutaway|Miniature reconstruction|Object interior reveal|Floating annotation|Tracked diagram|Cause-and-effect insert','Comedy composites':'Impossible prop|Sudden scale change|Duplicate character|Unexpected background|Object teleport cut|Surreal reality shift'}),
 'Palettes and design systems':('Genre-specific systems',{'Explainer kits':'Science color coding|Map colors|Business dashboard|Classroom diagram|Editorial fact cards|Mechanism labels','Music and comedy kits':'Lyric type hierarchy|Verse/chorus colors|Audio-reactive accents|Sketch title cards|Reaction captions|Meme frame borders'}),
 'Captions and localization':('Story-aware captions',{'Caption direction':'Reveal aligned with speech|Punchline withheld until spoken|Speaker change|Emphasis word|Sound cue caption|Narration pause','Subtitle assets':'Timed transcript|Translation draft|Pronunciation glossary|Speaker labels|Caption style preset|Safe-area preview'}),
 'Voiceover and narration':('Narration-to-visual planning',{'Performance direction':'Curiosity question|Tension build|Deadpan line|Warm reflection|Emphatic reveal|Quiet final thought','Cue packets':'Pronunciation sheet|Sentence timing|Pause map|Emphasis marks|Visual cue alignment|Pickup notes'})
 }
 for cat,(section,fams) in extra.items():
  for name,items in fams.items():group(cat,section,name,items)

# Move existing families into useful display folders while keeping their original IDs.
LAYOUTS={
 'Maps and geography':('Map system',{'Base maps and projections':['World and projection','Visual layers'],'Places and boundaries':['Borders and places','Physical geography'],'Transport and routes':['Transport networks'],'Camera and controls':['Animated moves','Controls and variants'],'Geographic data':['Data preparation']}),
 '2D assets':('Asset packs',{'People and objects':['People and characters','Objects'],'Devices and interface kits':['Devices','Interface kits','Icons'],'Environments and surfaces':['Environment','Textures and overlays']}),
 '3D assets':('Models and production',{'Devices and technology':['iPhone','Samsung and Android','Computers','Audio and wearables'],'Scenes and objects':['Objects and scenes'],'Materials and rigging':['Materials','Rigging and delivery']}),
 'Sound effects':('Sound families',{'Interface and technology':['UI feedback','Technology'],'Movement and impact':['Movement','Impacts and emphasis','Transition design'],'World and voice':['Nature and ambience','Voice']}),
 'Music':('Music collection',{'Mood and genre':['Mood','Genre'],'Scene scoring':['Use and structure'],'Stems and deliverables':['Production files']}),
 'Fonts and typography':('Font catalog',{'Reading fonts':['Sans serif','Serif'],'Expressive fonts':['Display and condensed','Handwritten and playful'],'Code and language support':['Monospace','Multilingual and symbols'],'Typography systems':['Type systems']}),
 'Transitions and effects':('Effect families',{'Scene transitions':['Cuts and spatial','Masks and reveals'],'Optical and digital effects':['Optical and texture','Digital and stylized'],'Morphs and finish':['Morph and physics','Color and finish']}),
 'Video formats and scenes':('Reusable sequences',{'Social formats':['Short form'],'Long-form formats':['Long form'],'Brand and broadcast':['Brand and product','Broadcast packages']}),
 'Production building blocks':('Reusable techniques',{'Camera and lighting':['Camera','Lighting'],'Motion and delivery':['Motion mechanics','Delivery']}),
 'Code recipes and integrations':('Implementation catalog',{'2D implementations':['2D and UI'],'3D and geography implementations':['3D and maps'],'Automation tools':['Automation']}),
 'Meme clips and reactions':('Reaction library',{'Reaction collections':['Reaction moods','Familiar reaction references','Animals and characters'],'Comic action and timing':['Comedic actions','Comedic timing'],'Clip formats and context':['Editing formats','Context and source notes']}),
 'Archival media and documents':('Evidence collections',{'Historical archive':['Historical material'],'Documents and evidence':['Evidence and documents'],'Source records':['Editorial source organization']}),
 'Photography and cutouts':('Still image collections',{'Photo subjects':['Portraits and people','Products and places'],'Layered images':['Cutouts and editorial assets'],'Photo motion preparation':['Photo animation preparation']}),
 'VFX and compositing':('Compositing library',{'Practical elements':['Practical visual elements'],'Masks and integration':['Keying and masks','Tracking and integration'],'Render passes':['Composite building blocks']}),
 'Palettes and design systems':('Reusable design recipes',{'Color and branding':['Color systems','Brand ingredients'],'Layouts and composition':['Layout recipes','Composition guides']}),
 'Storytelling and editing':('Editorial recipes',{'Core story mechanics':['Story beats','Pacing references'],'Story assembly':['Editing patterns','Sequence planning']}),
 'Captions and localization':('Text and accessibility',{'Caption looks':['Caption styles'],'Languages':['Localization'],'Accessibility and files':['Accessibility and delivery']}),
 'Voiceover and narration':('Narration library',{'Voice direction':['Voice direction'],'Recording and processing':['Voice production'],'Timing and alignment':['Alignment and assets']})
}
def organize(categories,slug):
 for category in categories:
  if category['name'] not in LAYOUTS:continue
  wrapper,groups=LAYOUTS[category['name']];old=next((x for x in category['children'] if x['name']==wrapper),None)
  if not old:continue
  remaining={x['name']:x for x in old['children']};replacements=[]
  for label,names in groups.items():
   children=[remaining.pop(n) for n in names if n in remaining]
   if children:replacements.append({'id':category['id']+'/folders/'+slug(label),'name':label,'children':children})
  if remaining:old['children']=list(remaining.values());replacements.append(old)
  index=category['children'].index(old);category['children'][index:index+1]=replacements
 for category in categories:
  if category['name']=='Storytelling and editing':category['name']='Storytelling'
  if category['name']=='Styles and inspiration':
   labels={'Editorial pacing':'Editorial cut rhythm','Diagram storytelling':'Diagram scene transitions','Question opener':'Question title treatment','Evidence reveal':'Evidence reveal graphics','Tension pacing':'Tension-driven cut rhythm','Measured pacing':'Measured edit rhythm','Product storytelling':'Product scene choreography'}
   def relabel(node):
    node['name']=labels.get(node['name'],node['name'])
    for child in node.get('children',[]):relabel(child)
   relabel(category)
 return categories
