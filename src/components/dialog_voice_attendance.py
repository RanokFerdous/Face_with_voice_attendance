# import streamlit as st

# from src.pipelines.voice_pipeline import process_bulk_audio

# from src.database.config import supabase

# import pandas as pd


# from src.components.dialog_attendance_results import show_attendance_result
# from datetime import datetime
# @st.dialog('Voice Attendance')
# def voice_attendance_dialog(selected_subject_id):
#     st.write('Record audio of students saying I am present. Then AI will recognize the students')


#     audio_data = None

#     audio_data = st.audio_input("Record classroom audio")

#     if st.button('Analyze Audio', width='stretch', type='primary'):
#         with st.spinner('Prcessing Audio data'):
#             enrolled_res = supabase.table('subject_students').select("*, students(*)").eq('subject_id',selected_subject_id ).execute()
#             enrolled_students = enrolled_res.data

#             if not enrolled_students:
#                 st.warning('No students enrolled in this course')
#                 return
#             candidates_dict = {
#                 s['students']['student_id'] : s['students']['voice_embedding'] 
#                 for s in enrolled_students if s['students'].get('voice_embedding')
#             }

#             if not candidates_dict:
#                 st.error('No enrolled students have voice profiles registerd')
#                 return
            
#             audio_bytes = audio_data.read()

#             detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

#             results, attendance_to_log  = [], []

#             current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


#             for node in enrolled_students:
#                 student = node['students']
#                 score  = detected_scores.get(student['student_id'], 0.0)
#                 is_present= bool(score>0)

#                 results.append({
#                     "Name": student['name'],
#                     "ID": student['student_id'],
#                     "Source": score if is_present else "-",
#                     "Status": "✅ Present" if is_present else "❌ Absent"
#                 })

#                 attendance_to_log.append({
#                     'student_id': student['student_id'],
#                     'subject_id': selected_subject_id,
#                     'timestamp': current_timestamp,
#                     'is_present': bool(is_present)
#                 })
#             st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

#     if st.session_state.get('voice_attendance_results'):
#         st.divider()
#         df_results, logs = st.session_state.voice_attendance_results
#         show_attendance_result(df_results, logs)




# =======================================================

# import streamlit as st

# from src.pipelines.voice_pipeline import process_bulk_audio
# from src.database.config import supabase

# import pandas as pd

# from src.components.dialog_attendance_results import show_attendance_result
# from datetime import datetime


# @st.dialog('Voice Attendance')
# def voice_attendance_dialog(selected_subject_id):

#     st.write(
#         'Record audio of students saying I am present. '
#         'Then AI will recognize the students.'
#     )

#     # Widget for recording classroom audio
#     audio_data = st.audio_input("Record classroom audio")

#     # Analyze button
#     if st.button('Analyze Audio', width='stretch', type='primary'):

#         # STEP 1: Check whether audio was recorded
#         if audio_data is None:
#             st.warning("Please record classroom audio before analyzing!")
#             st.stop()

#         with st.spinner('Processing audio data...'):

#             # STEP 2: Get students enrolled in this subject
#             enrolled_res = (
#                 supabase.table('subject_students')
#                 .select("*, students(*)")
#                 .eq('subject_id', selected_subject_id)
#                 .execute()
#             )

#             enrolled_students = enrolled_res.data

#             # Check whether students are enrolled
#             if not enrolled_students:
#                 st.warning('No students enrolled in this course')
#                 st.stop()

#             # STEP 3: Collect voice embeddings of enrolled students
#             candidates_dict = {
#                 s['students']['student_id']: s['students']['voice_embedding']
#                 for s in enrolled_students
#                 if s['students'].get('voice_embedding')
#             }

#             # Check whether enrolled students have voice profiles
#             if not candidates_dict:
#                 st.error('No enrolled students have registered voice profiles')
#                 st.stop()

#             # STEP 4: Read recorded audio
#             audio_bytes = audio_data.read()

#             # Check whether the audio file contains data
#             if not audio_bytes:
#                 st.error("The recorded audio is empty. Please record again.")
#                 st.stop()

#             # STEP 5: Process audio using AI voice recognition
#             detected_scores = process_bulk_audio(
#                 audio_bytes,
#                 candidates_dict
#             )

#             # STEP 6: Prepare attendance results
#             results = []
#             attendance_to_log = []

#             current_timestamp = datetime.now().strftime(
#                 "%Y-%m-%dT%H:%M:%S"
#             )

#             for node in enrolled_students:

#                 student = node['students']

#                 score = detected_scores.get(
#                     student['student_id'],
#                     0.0
#                 )

#                 is_present = bool(score > 0)

#                 results.append({
#                     "Name": student['name'],
#                     "ID": student['student_id'],
#                     "Source": score if is_present else "-",
#                     "Status": "Present" if is_present else "Absent"
#                 })

#             # STEP 7: Display attendance results
#             # Keep your existing result-saving logic here if present
#             show_attendance_result(results)

# ================================



import streamlit as st

from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase

from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime


@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):

    st.write(
        'Record audio of students saying I am present. '
        'Then AI will recognize the students.'
    )

    # Record classroom audio
    audio_data = st.audio_input("Record classroom audio")

    # Analyze recorded audio
    if st.button('Analyze Audio', width='stretch', type='primary'):

        # Check whether audio exists
        if audio_data is None:
            st.warning("Please record classroom audio first!")
            st.stop()

        with st.spinner('Processing audio data...'):

            # Get all students enrolled in this subject
            enrolled_res = (
                supabase.table('subject_students')
                .select("*, students(*)")
                .eq('subject_id', selected_subject_id)
                .execute()
            )

            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled in this course.')
                st.stop()

            # Get enrolled students' voice embeddings
            candidates_dict = {
                s['students']['student_id']: s['students']['voice_embedding']
                for s in enrolled_students
                if s['students'].get('voice_embedding')
            }

            if not candidates_dict:
                st.error('No enrolled students have registered voice profiles.')
                st.stop()

            # Read recorded audio
            audio_bytes = audio_data.read()

            if not audio_bytes:
                st.error("The recorded audio is empty. Please record again.")
                st.stop()

            # Run AI voice recognition
            detected_scores = process_bulk_audio(
                audio_bytes,
                candidates_dict
            )

            # Prepare attendance results and database logs
            results = []
            attendance_to_log = []

            current_timestamp = datetime.now().strftime(
                "%Y-%m-%dT%H:%M:%S"
            )

            for node in enrolled_students:

                student = node['students']
                student_id = student['student_id']

                # Get the voice recognition score
                score = detected_scores.get(student_id, 0.0)

                # Determine attendance status
                is_present = bool(score > 0)

                # Prepare data for the results table
                results.append({
                    "Name": student['name'],
                    "ID": student_id,
                    "Source": score if is_present else "-",
                    "Status": "Present" if is_present else "Absent"
                })

                # Prepare data for Supabase
                attendance_to_log.append({
                    "timestamp": current_timestamp,
                    "subject_id": selected_subject_id,
                    "student_id": student_id,
                    "is_present": is_present
                })

            # Display results and wait for teacher confirmation
            show_attendance_result(results, attendance_to_log)
