import java.util.Scanner;

public class StudentAIChatbot {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("=================================");
        System.out.println("     AI STUDENT LIFE CHATBOT");
        System.out.println("=================================");
        System.out.println("Hello! I am your AI Student Assistant.");
        System.out.println("Type 'exit' to close the chatbot.");
        System.out.println();

        while (true) {

            System.out.print("You: ");
            String question = sc.nextLine().toLowerCase();

            if (question.equals("exit")) {
                System.out.println("AI: Goodbye! All the best for your studies!");
                break;
            }

            if (question.contains("study") ||
                question.contains("exam")) {

                System.out.println(
                    "AI: Make a study plan by dividing your subjects "
                    + "into small topics. Study for 45 minutes and "
                    + "take a 10-minute break."
                );

            } else if (question.contains("java")) {

                System.out.println(
                    "AI: For Java, start with variables, conditions, "
                    + "loops, methods, OOP and then practice programs."
                );

            } else if (question.contains("interview")) {

                System.out.println(
                    "AI: Prepare your introduction, Java basics, "
                    + "DSA basics and questions about your projects."
                );

            } else if (question.contains("stress") ||
                       question.contains("tired")) {

                System.out.println(
                    "AI: Take a short break, drink some water and "
                    + "divide your work into smaller tasks."
                );

            } else if (question.contains("timetable") ||
                       question.contains("schedule")) {

                System.out.println(
                    "AI: Start with your important subjects first. "
                    + "Keep separate time for coding, revision and breaks."
                );

            } else if (question.contains("hello") ||
                       question.contains("hi")) {

                System.out.println(
                    "AI: Hello! How can I help you with your student life?"
                );

            } else {

                System.out.println(
                    "AI: I am still learning. Try asking about "
                    + "study, exams, Java, interviews, timetable or stress."
                );
            }
        }

        sc.close();
    }
}