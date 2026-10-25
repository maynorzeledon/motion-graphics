"""Joke structures and delivery references, kept separate from visual editing styles."""
JOKES={
'Dad jokes':('Corny question-and-answer pun|Homophone misunderstanding|Familiar phrase with a silly twist|Overly obvious literal answer|Groan-worthy word substitution|Wholesome everyday setup','Earnest delivery|Pause before the obvious pun|Reaction after the punchline'),
'Puns and wordplay':('Homophones|Multiple word meanings|Compound-word split|Name-based wordplay|Sound-alike substitution|Word blending','Emphasize the pivot word|Reveal the alternate meaning|Let the audience resolve the pun'),
'One-liners':('Compressed setup and payoff|Unexpected final word|Short comparison|Single-sentence reversal','Trim unnecessary setup|Place the strongest word last|Pause after the line'),
'Knock-knock jokes':('Standard call-and-response|Name becomes a phrase|Interrupting response|Repeated sound payoff','Alternate speakers clearly|Keep the expected rhythm|Break the rhythm for the payoff'),
'Anti-jokes and anticlimax':('Ordinary answer to a joke-shaped question|Deliberately mundane outcome|Setup promises more than the ending|Refusal of the expected punchline','Straight-faced delivery|Hold the unremarkable result|Let the missing payoff be the joke'),
'Deadpan and dry humor':('Absurd statement presented seriously|Deliberate understatement|Calm reaction to chaos|Matter-of-fact contradiction','Neutral expression|Restrained voice|Leave space after the statement'),
'Misdirection and reversals':('Expected explanation replaced|Ambiguous setup resolved differently|Final word changes the meaning|Apparent problem becomes an advantage','Guide the first interpretation|Delay the key detail|Make the reveal understandable'),
'Observational jokes':('Recognizable everyday habit|Tiny annoyance exaggerated|Unspoken social rule|Odd detail everyone overlooks','Start with a concrete example|Use precise relatable details|Finish with a fresh comparison'),
'Absurdist and surreal jokes':('Impossible event treated as normal|Unrelated ideas joined by strange logic|Ordinary rule applied to an impossible world|Reality changes without explanation','Commit to the internal logic|Keep character reactions consistent|Use the ending to reframe the setup'),
'Visual gags':('Background detail contradicts dialogue|Unexpected object reveal|Scale mismatch|Image completes a spoken phrase','Control what is visible|Choose the revealing frame|Hold long enough to notice'),
'Slapstick and physical comedy':('Exaggerated movement|Prop mishap|Clumsy recovery|Chain reaction|Near miss followed by a harmless surprise','Readable body staging|Anticipation before action|Reaction after the physical payoff'),
'Self-deprecating humor':('Small personal mistake|Overconfident setup meets reality|Contradiction in one’s own behavior|Harmless awkward confession','Keep the target specific|Avoid turning the bit into self-loathing|End on a shared human observation'),
'Sarcasm and verbal irony':('Say the opposite of the visible situation|Overpraise an obviously tiny achievement|Polite words with a clear comic mismatch|Mock-serious agreement','Make the intended meaning readable|Match the audience context|Compare sincere and sarcastic versions'),
'Situational and dramatic irony':('Outcome contradicts the plan|Audience knows something the character does not|Attempted solution creates the problem|Confident prediction immediately fails','Establish the expectation|Give the audience the needed information|Pay off the contrast'),
'Parody and spoof':('Recognizable genre convention exaggerated|Commercial format used for a trivial object|Dramatic trailer for an ordinary task|Tutorial format applied to an absurd skill','Establish the borrowed format|Choose a specific convention to exaggerate|Keep the joke legible without copying a full script'),
'Satire':('Exaggerated rule exposes a contradiction|Ironic comparison of stated goals and behavior|Fictional scenario highlights a real pattern|Mock announcement reveals an absurd incentive','Choose a clear subject|Make the point through the situation|Distinguish the fictional scenario from a factual claim'),
'Rule of three':('Two ordinary items establish a pattern|Third item breaks the pattern|Third repetition changes the stakes|Three-step escalation','Match the first two beats|Give the third beat emphasis|Avoid explaining the surprise'),
'Callbacks and running gags':('Return to an earlier line|Recurring prop|Repeated character mistake|Earlier detail becomes the final payoff','Track the original setup|Vary each repetition|Use the strongest callback near the ending'),
'Misunderstanding and crossed wires':('One phrase has two interpretations|Characters assume different situations|Unclear pronoun creates confusion|Instruction followed in the wrong context','Establish both interpretations|Escalate the consequences|Resolve or reveal the crossed assumptions'),
'Escalation and exaggeration':('Small problem grows through repeated attempts|Increasingly specific excuse|Ordinary claim becomes wildly exaggerated|Character doubles down on a silly rule','Start with a readable baseline|Change the scale each beat|Finish at the strongest understandable version'),
'Meta and self-aware humor':('Character notices the video format|Narrator comments on the joke structure|Caption disagrees with the speaker|Creator interrupts an expected editing convention','Establish the convention first|Choose the moment to acknowledge it|Return to the scene after the interruption'),
'Shaggy-dog stories and long-form anti-payoffs':('Over-detailed ordinary story|Repeated detours before a tiny ending|Elaborate setup for a simple pun|Deliberately disproportionate setup and payoff','Make each detour intentional|Track audience expectations|Decide whether the ending rewards the long setup')
}
def extend_jokes(group):
 for name,(mechanics,delivery) in JOKES.items():
  group('Storytelling and editing','Comedy formats',name,{
   'Mechanics and patterns':mechanics.split('|'),
   'Timing and delivery':delivery.split('|'),
   'Reference studies':['Original video or joke reference','Setup → pivot → punchline breakdown','Reusable script and visual blueprint']
  })
