import cv2
import mediapipe as mp


mp_face_mesh = mp.solutions.face_mesh


def start_attention_tracking():

    cap = cv2.VideoCapture(0)

    face_mesh = mp_face_mesh.FaceMesh(
        max_num_faces=2,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    mp_draw = mp.solutions.drawing_utils
    mp_style = mp.solutions.drawing_styles

    # ---------------- STABLE VARIABLES ----------------
    center_x_ref = None
    center_y_ref = None

    last_direction = "CENTER"
    distraction_count = 0

    alpha = 0.95  # smoothing factor

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)
        # ---------------- MULTIPLE FACE WARNING ----------------
        if results.multi_face_landmarks:
           if len(results.multi_face_landmarks) > 1:
            cv2.putText(frame, "WARNING: MULTIPLE FACES DETECTED!",
                    (10, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3)

        direction = "NO FACE"

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:
                

                mp_draw.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_TESSELATION,
                    None,
                    mp_style.get_default_face_mesh_tesselation_style()
                )

                lm = face_landmarks.landmark

                # ---------------- NOSE POINT ----------------
                nose_x = lm[1].x
                nose_y = lm[1].y

                # ---------------- INIT CENTER ----------------
                if center_x_ref is None:
                    center_x_ref = nose_x
                    center_y_ref = nose_y

                # ---------------- SMOOTH CENTER (NO NOISE) ----------------
                center_x_ref = alpha * center_x_ref + (1 - alpha) * nose_x
                center_y_ref = alpha * center_y_ref + (1 - alpha) * nose_y

                dx = nose_x - center_x_ref
                dy = nose_y - center_y_ref

                # ---------------- DIRECTION LOGIC ----------------
                if dx < -0.035:
                    direction = "LEFT"
                elif dx > 0.035:
                    direction = "RIGHT"
                elif dy < -0.04:
                    direction = "UP"
                elif dy > 0.06:
                    direction = "DOWN"
                else:
                    direction = "CENTER"

                # ---------------- DISCTRACTION COUNT ----------------
                if direction != "CENTER" and last_direction == "CENTER":
                    distraction_count += 1

                last_direction = direction

        # ---------------- UI ----------------
        cv2.putText(frame, f"Look: {direction}", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(frame, f"Distractions: {distraction_count}", (10, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("PRO Attention Tracker (Fixed)", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# ---------------- RUN ----------------
start_attention_tracking()