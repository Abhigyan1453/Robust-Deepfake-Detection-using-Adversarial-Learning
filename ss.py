from graphviz import Digraph

dot = Digraph(comment='Deepfake Detection System Architecture')

dot.attr(rankdir='LR')  # Left to right

# Define nodes
dot.node('A', 'Input Image')
dot.node('B', 'Face Extraction & Preprocessing\n- Face Detection\n- Alignment\n- Normalization')
dot.node('C', 'Feature Extraction Network\n- Generator\n- Discriminator')
dot.node('D', 'Classification & Decision Module\n- Real/Fake\n- Confidence Score')

# Define edges
dot.edge('A', 'B')
dot.edge('B', 'C')
dot.edge('C', 'D')
dot.edge('B', 'D', constraint='false')  # optional shortcut
dot.edge('D', 'B', style='dashed', label='Feedback Loop')

# Render and save
dot.render('architecture_diagram', format='png', view=True)
