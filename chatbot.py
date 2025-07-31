import streamlit as st
from openai import OpenAI

# Get secret from Streamlit secrets.toml
api_key = st.secrets["OPENAI_API_KEY"]
if not api_key:
    st.error("OPENAI_API_KEY is not set in .streamlit/secrets.toml.")
    st.stop()

client = OpenAI(api_key=api_key)
englishunitdata = {
  "Kindergarten": [
    "Unit 1: Concepts of Print and Phonological Awareness",
    "Unit 2: Understanding Story Elements",
    "Unit 3: Writing to Express Opinions",
    "Unit 4: Exploring Informational Texts",
    "Unit 5: Speaking and Listening Through Shared Reading"
  ],
  "Grade 1": [
    "Unit 1: Phonics and Word Recognition",
    "Unit 2: Reading Stories and Characters",
    "Unit 3: Opinion and Narrative Writing",
    "Unit 4: Informational Text and Text Features",
    "Unit 5: Listening, Speaking, and Collaboration"
  ],
  "Grade 2": [
    "Unit 1: Building Reading Fluency",
    "Unit 2: Understanding Characters and Plot",
    "Unit 3: Writing to Inform and Explain",
    "Unit 4: Exploring Nonfiction Text Structures",
    "Unit 5: Speaking, Listening, and Research"
  ],
  "Grade 3": [
    "Unit 1: Reading Comprehension Strategies",
    "Unit 2: Analyzing Characters and Themes",
    "Unit 3: Writing Opinion Pieces",
    "Unit 4: Understanding Informational Texts",
    "Unit 5: Research and Presentation Skills"
  ],
  "Grade 4": [
    "Unit 1: Reading Literary and Informational Texts",
    "Unit 2: Comparing Themes and Topics",
    "Unit 3: Writing Narrative and Expository Texts",
    "Unit 4: Using Text Evidence",
    "Unit 5: Collaborative Discussions and Presentations"
  ],
  "Grade 5": [
    "Unit 1: Summarizing and Analyzing Texts",
    "Unit 2: Literary Elements and Point of View",
    "Unit 3: Writing Opinion and Informative Essays",
    "Unit 4: Integrating Information from Multiple Sources",
    "Unit 5: Effective Speaking and Listening"
  ],
  "Grade 6": [
    "Unit 1: Analyzing Plot and Setting",
    "Unit 2: Reading and Writing Informative Texts",
    "Unit 3: Argument Writing and Evidence",
    "Unit 4: Comparing Literary and Informational Texts",
    "Unit 5: Collaborative Discussion and Media Literacy"
  ],
  "Grade 7": [
    "Unit 1: Understanding Literary Elements",
    "Unit 2: Analyzing Author's Purpose and Perspective",
    "Unit 3: Writing Structured Arguments",
    "Unit 4: Evaluating Claims and Evidence",
    "Unit 5: Research Projects and Speaking Skills"
  ],
  "Grade 8": [
    "Unit 1: Literary Analysis and Theme",
    "Unit 2: Reading and Writing Informational Texts",
    "Unit 3: Argumentative Writing and Rhetoric",
    "Unit 4: Integrating Multimedia and Research",
    "Unit 5: Speaking and Listening in Academic Settings"
  ],
  "Grade 9": [
    "Unit 1: Analyzing Complex Characters and Conflicts",
    "Unit 2: Writing Literary Analyses",
    "Unit 3: Argument Writing and Rhetorical Appeals",
    "Unit 4: Synthesizing Sources in Research",
    "Unit 5: Presentation and Collaborative Discussion"
  ],
  "Grade 10": [
    "Unit 1: Analyzing Theme and Central Ideas",
    "Unit 2: Evaluating Argument and Rhetorical Strategies",
    "Unit 3: Informative and Analytical Writing",
    "Unit 4: Researching and Citing Sources",
    "Unit 5: Academic Discussions and Presentations"
  ],
  "Grade 11": [
    "Unit 1: American Literature and Historical Context",
    "Unit 2: Analyzing Persuasion and Argument",
    "Unit 3: Writing Synthesis Essays",
    "Unit 4: Research Writing and Source Evaluation",
    "Unit 5: Debates and Formal Presentations"
  ],
  "Grade 12": [
    "Unit 1: British and World Literature",
    "Unit 2: Critical Literary Analysis",
    "Unit 3: Crafting College and Career Writing",
    "Unit 4: Argument and Ethical Reasoning",
    "Unit 5: Capstone Research and Presentation"
  ]
}
scienceunitdata = {
  "Kindergarten": [
    "Unit 1: Weather Patterns and Seasons",
    "Unit 2: Forces and Motion: Pushes and Pulls",
    "Unit 3: Living Things and Their Needs",
    "Unit 4: Exploring the Five Senses",
    "Unit 5: Earth Materials and Their Uses"
  ],
  "Grade 1": [
    "Unit 1: Patterns in Space: Sun, Moon, and Stars",
    "Unit 2: Sound and Light",
    "Unit 3: Plant and Animal Structures",
    "Unit 4: Properties of Matter",
    "Unit 5: Environmental Impacts and Solutions"
  ],
  "Grade 2": [
    "Unit 1: Earth’s Landforms and Water",
    "Unit 2: Changing States of Matter",
    "Unit 3: Life Cycles of Plants and Animals",
    "Unit 4: Magnetism and Motion",
    "Unit 5: Human Impact on Earth"
  ],
  "Grade 3": [
    "Unit 1: Forces and Motion: Balanced and Unbalanced",
    "Unit 2: Inheritance and Traits",
    "Unit 3: Weather and Climate",
    "Unit 4: Organisms and Their Habitats",
    "Unit 5: Life Cycles and Adaptations"
  ],
  "Grade 4": [
    "Unit 1: Energy and Motion",
    "Unit 2: Waves and Information Transfer",
    "Unit 3: Internal and External Structures of Living Things",
    "Unit 4: Earth's Surface Processes",
    "Unit 5: Renewable and Nonrenewable Resources"
  ],
  "Grade 5": [
    "Unit 1: Properties of Matter and Chemical Reactions",
    "Unit 2: Ecosystems and Energy Flow",
    "Unit 3: Earth Systems: Geosphere, Hydrosphere, Atmosphere",
    "Unit 4: The Solar System and Space Exploration",
    "Unit 5: Engineering Design and Solutions"
  ],
  "Grade 6": [
    "Unit 1: Cells and Microorganisms",
    "Unit 2: Energy in Earth's Systems",
    "Unit 3: Weather and Climate Systems",
    "Unit 4: Forces and Motion in the Physical World",
    "Unit 5: Human Body Systems and Health"
  ],
  "Grade 7": [
    "Unit 1: Structure and Function of Cells",
    "Unit 2: Genetics and Heredity",
    "Unit 3: Earth's History and Fossil Record",
    "Unit 4: Chemical Reactions and Matter",
    "Unit 5: Ecosystem Interactions and Biodiversity"
  ],
  "Grade 8": [
    "Unit 1: Forces and Newton’s Laws",
    "Unit 2: Atoms, Elements, and the Periodic Table",
    "Unit 3: Natural Selection and Evolution",
    "Unit 4: Earth's Systems and Plate Tectonics",
    "Unit 5: Energy Transfer and Conservation"
  ],
  "Grade 9": [
    "Unit 1: Scientific Inquiry and Lab Skills",
    "Unit 2: Matter and Chemical Bonding",
    "Unit 3: Cell Structure, Function, and Energy",
    "Unit 4: Newtonian Physics",
    "Unit 5: Ecology and Human Impact"
  ],
  "Grade 10": [
    "Unit 1: Atomic Theory and Periodicity",
    "Unit 2: Genetics and Molecular Biology",
    "Unit 3: Thermodynamics and Energy Systems",
    "Unit 4: Evolution and Biodiversity",
    "Unit 5: Earth and Space Science"
  ],
  "Grade 11": [
    "Unit 1: Quantum Chemistry and Chemical Reactions",
    "Unit 2: Human Body Systems and Homeostasis",
    "Unit 3: Electricity and Magnetism",
    "Unit 4: Environmental Science and Sustainability",
    "Unit 5: Scientific Research and Experimental Design"
  ],
  "Grade 12": [
    "Unit 1: Advanced Genetics and Biotechnology",
    "Unit 2: Mechanics and Wave Physics",
    "Unit 3: Climate Science and Earth’s Future",
    "Unit 4: Systems Biology and Interdependence",
    "Unit 5: Capstone Science Research Project"
  ]
}
historyunitdata = {
  "Kindergarten": [
    "Unit 1: Understanding Time and Change",
    "Unit 2: Family and Community Traditions",
    "Unit 3: National Holidays and Symbols",
    "Unit 4: Rules and Responsibilities",
    "Unit 5: Community Helpers and Leaders"
  ],
  "Grade 1": [
    "Unit 1: Comparing Past and Present",
    "Unit 2: American Symbols and Landmarks",
    "Unit 3: Timelines and Personal History",
    "Unit 4: Influential Americans",
    "Unit 5: Celebrations and Traditions Around the World"
  ],
  "Grade 2": [
    "Unit 1: Local History and Communities",
    "Unit 2: Geography and Map Skills",
    "Unit 3: Civic Responsibilities and Rules",
    "Unit 4: Historical Figures and Inventors",
    "Unit 5: Culture and Diversity"
  ],
  "Grade 3": [
    "Unit 1: Early Communities and Indigenous Peoples",
    "Unit 2: Exploration and Colonization",
    "Unit 3: Government and Citizenship",
    "Unit 4: Local and Regional History",
    "Unit 5: Economics and Trade in Communities"
  ],
  "Grade 4": [
    "Unit 1: Geography of the United States",
    "Unit 2: Native American Cultures",
    "Unit 3: Colonial America",
    "Unit 4: American Revolution",
    "Unit 5: U.S. Government and Constitution"
  ],
  "Grade 5": [
    "Unit 1: Early Exploration and Settlement",
    "Unit 2: Founding of the United States",
    "Unit 3: Westward Expansion",
    "Unit 4: Civil War and Reconstruction",
    "Unit 5: Immigration and Industrial Growth"
  ],
  "Grade 6": [
    "Unit 1: Ancient Civilizations: Mesopotamia, Egypt, and the Indus Valley",
    "Unit 2: Ancient China and India",
    "Unit 3: Ancient Greece and Rome",
    "Unit 4: World Religions and Philosophies",
    "Unit 5: Fall of Empires and the Middle Ages"
  ],
  "Grade 7": [
    "Unit 1: The Renaissance and Reformation",
    "Unit 2: Exploration and Colonization",
    "Unit 3: Enlightenment and Revolutions",
    "Unit 4: Industrial Revolution and Imperialism",
    "Unit 5: World Wars and Global Conflict"
  ],
  "Grade 8": [
    "Unit 1: Colonial America and the Road to Revolution",
    "Unit 2: Founding Documents and the Constitution",
    "Unit 3: Expansion and Reform in the 1800s",
    "Unit 4: Civil War and Reconstruction",
    "Unit 5: The Gilded Age and Progressive Era"
  ],
  "Grade 9": [
    "Unit 1: Foundations of World History",
    "Unit 2: Classical Civilizations and Empires",
    "Unit 3: Global Exchange and Colonization",
    "Unit 4: Modern Revolutions",
    "Unit 5: Nationalism and the Rise of Nation-States"
  ],
  "Grade 10": [
    "Unit 1: Causes and Consequences of World War I",
    "Unit 2: Interwar Period and Totalitarianism",
    "Unit 3: World War II",
    "Unit 4: The Cold War and Decolonization",
    "Unit 5: Contemporary Global Issues"
  ],
  "Grade 11": [
    "Unit 1: Foundations of American Democracy",
    "Unit 2: Civil War and Reconstruction",
    "Unit 3: Industrialization and Urbanization",
    "Unit 4: U.S. in the World Wars",
    "Unit 5: Civil Rights and Modern America"
  ],
  "Grade 12": [
    "Unit 1: Origins and Functions of U.S. Government",
    "Unit 2: Supreme Court Cases and Civil Liberties",
    "Unit 3: U.S. Foreign Policy and Global Role",
    "Unit 4: Economic Systems and Policy Decisions",
    "Unit 5: Civic Engagement and Current Events"
  ]
}

mathunitdata = {
  "Kindergarten": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 1": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 2": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 3": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 4": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 5": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 6": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 7": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 8": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 9": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 10": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 11": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ],
  "Grade 12": [
    "Unit 1: Number Sense and Operations",
    "Unit 2: Algebraic Thinking and Patterns",
    "Unit 3: Geometry and Spatial Reasoning",
    "Unit 4: Measurement and Data",
    "Unit 5: Problem Solving and Applications"
  ]
}


st.title("OpenAI Chatbot")
grade_level=st.selectbox("Select Grade Level", 
    ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "Grade 9", "Grade 10", "Grade 11", "Grade 12"])
subject=st.selectbox("Select Subject",
    ["Math", "Science", "History", "English"])
if subject == "Math": 
    unit=st.selectbox("Select Unit", 
        mathunitdata[grade_level])
if subject == "English": 
  unit=st.selectbox("Select Unit", 
      englishunitdata[grade_level])
if subject == "Science": 
  unit=st.selectbox("Select Unit", 
      scienceunitdata[grade_level])
if subject == "History": 
  unit=st.selectbox("Select Unit", 
      historyunitdata[grade_level])
  
  

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Specify further details for the worksheet.")
if user_input:

    user_input = "make a " + grade_level + " " + subject + " worksheet with " + user_input  # Debugging line to check user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=st.session_state.messages
        )
        bot_reply = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})
        st.chat_message("assistant").write(bot_reply)