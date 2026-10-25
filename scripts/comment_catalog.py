"""Collection targets for context-aware comments, replies, and community voices."""
def extend_comments(group):
 sections={
 'Gen Z and internet humor':{
 'Casual voices':'Lowercase conversational|Dry understatement|Playful exaggeration|Self-aware reaction|Mock-serious analysis|Wholesome internet humor',
 'Absurdist replies':'Unexpected comparison|Overly literal interpretation|Escalate one tiny detail|Invent a silly explanation|Treat a small moment as a major event|Surreal callback',
 'Internet language studies':'Slang used naturally|Slang-free alternative|Emoji as punctuation|Emoji-free alternative|Short reaction phrase|Context-specific meme reference|Dated slang notes|Community-specific vocabulary'},
 'Brand replies':{
 'Brand personalities':'Playful and witty|Warm and helpful|Premium and restrained|Bold challenger|Wholesome and supportive|Technical expert|Minimal and direct|Friendly local business',
 'Community interactions':'Respond to a joke|Celebrate a customer|Answer a product question|Acknowledge useful feedback|Reply to a creator mention|Join a relevant trend|Thank someone naturally|Give credit',
 'Service and sensitive replies':'Clarify confusion|Acknowledge a mistake|Apologize with a concrete next step|Explain a limitation|Move private details to support|Set a calm boundary|Respond to criticism|Follow up after resolution'},
 'Comedy and wordplay':{
 'Joke structures':'Callback to the video|Setup and punchline|Literal joke|Double meaning|Word substitution|Unexpected analogy|Rule of three|Reversal|Anti-joke|Understatement',
 'Delivery styles':'One-line deadpan|Short dramatic reaction|Over-specific observation|Mock formal reply|Friendly self-deprecation|Playful compliment|Gentle situational roast|Unexpected sincere ending',
 'Reference patterns':'Quote a specific moment|Notice a background detail|Connect the ending to the opening|Continue the premise|Answer the unspoken question|Subvert an expected response'},
 'Thoughtful and supportive':{
 'Positive replies':'Specific compliment|Recognize effort|Encourage progress|Celebrate a milestone|Appreciate a useful explanation|Support a difficult moment',
 'Useful contributions':'Add relevant context|Ask a genuine question|Offer a concise clarification|Share a relevant resource|Summarize a useful takeaway|Connect two ideas',
 'Disagreement and correction':'Respectful disagreement|Ask for evidence|Correct a factual detail|Acknowledge uncertainty|Find common ground|Clarify a misunderstanding'},
 'Video context and audience':{
 'Entertainment contexts':'Comedy sketch|Surreal sketch|Literal joke video|Meme edit|Gaming highlight|Sports moment|Music performance|Lyric video|Pet video|Unexpected ending',
 'Informative contexts':'Science explainer|History documentary|Map video|Technology review|Product demonstration|Tutorial|School project|News explanation',
 'Human and brand contexts':'Personal achievement|Travel story|Food and recipe|Creative process|Small business post|Customer story|Creator collaboration|Serious personal update'},
 'Platforms and thread formats':{
 'Comment formats':'Top-level comment|Reply to creator|Reply to another viewer|Pinned comment|Creator follow-up|Answer to a question|Short one-liner|Two-sentence response',
 'Platform reference folders':'Instagram Reels examples|TikTok examples|YouTube Shorts examples|YouTube long-form examples|Reddit thread examples|Facebook post examples|X reply examples',
 'Conversation patterns':'Keep a running joke going|Answer then add a detail|Reference the parent comment|Clarify your earlier reply|Repair a misread tone|Close a resolved conversation'},
 'Reference examples and analysis':{
 'Example packets':'Original video or source link|Video transcript or summary|Relevant timestamp|Comment-thread screenshot|Parent comment text|Reply text|Creator or brand voice notes|Why the reply fits',
 'Observed response records':'Like count at observation|Reply count at observation|Posting date|Observation date|Pinned status|Creator response|Audience context|Platform context|Uncertainty about why it performed',
 'Reusable blueprints':'Video detail → concise reaction|Parent comment → callback|Question → helpful answer|Misunderstanding → clarification|Brand mention → personality plus usefulness|Setup → literal visual reference'},
 'Writing and selection workflow':{
 'Understand the context':'Watch or read the actual content|Identify the strongest specific detail|Read the parent comment|Identify the intended audience|Check whether humor fits|Choose language and register',
 'Draft candidates':'Write a concise version|Write a witty version|Write a thoughtful version|Write a brand-voice version|Write a slang-free version|Preserve the intended meaning',
 'Evaluate and refine':'Specificity to this video|Naturalness|Brevity|Clarity of the joke|Fit with parent comment|Voice consistency|Avoid a repeated generic line|Avoid invented personal experience|Check factual claims|Remove forced slang'},
 'Languages and cultural context':{
 'Language variants':'English casual|Spanish casual|Bilingual reply|English deadpan|Spanish wordplay|Translate the intent rather than each word',
 'Voice calibration':'Match the audience vocabulary|Explain a local reference in notes|Keep an expression in its original language|Record regional meaning|Neutral-language alternative|Compare sincere and sarcastic readings'}
 }
 for section,families in sections.items():
  for name,items in families.items():group('Comments and replies',section,name,items)
