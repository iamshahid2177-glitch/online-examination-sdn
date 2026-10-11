import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

questions = [
    ("What is the capital of India?", "Delhi"),
    ("What does TCP stand for?", "Transmission Control Protocol"),
    ("What is 5 + 5?", "10")
]


def handle_client(conn, addr):
    print(f"[CONNECTED] {addr}")

    reader = conn.makefile("r")
    writer = conn.makefile("w")

    try:
        writer.write("Welcome to the Online Examination System!\n")
        writer.flush()

        score = 0

        for i, (question, answer) in enumerate(questions, 1):

            writer.write(f"Q{i}. {question}\n")
            writer.flush()

            client_answer = reader.readline().strip()

            if client_answer.lower() == answer.lower():
                score += 1
                writer.write("Correct!\n")
            else:
                writer.write(f"Wrong! Correct answer: {answer}\n")

            writer.flush()

        writer.write(f"Exam completed. Score: {score}/{len(questions)}\n")
        writer.flush()

    except Exception as e:
        print(f"[ERROR] {addr}: {e}")

    finally:
        reader.close()
        writer.close()
        conn.close()
        print(f"[DISCONNECTED] {addr}")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))
server.listen(10)

print(f"[SERVER] Listening on port {PORT}...")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    thread.start()
