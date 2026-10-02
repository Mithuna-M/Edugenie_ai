const taskButtons =
    document.querySelectorAll(".task-button");

const form =
    document.getElementById("eduForm");

const userInput =
    document.getElementById("userInput");

const levelContainer =
    document.getElementById("levelContainer");

const level =
    document.getElementById("level");

const inputLabel =
    document.getElementById("inputLabel");

const submitButton =
    document.getElementById("submitButton");

const submitText =
    document.getElementById("submitText");

const loadingSpinner =
    document.getElementById("loadingSpinner");

const characterCount =
    document.getElementById("characterCount");

const resultSection =
    document.getElementById("resultSection");

const resultTitle =
    document.getElementById("resultTitle");

const resultContent =
    document.getElementById("resultContent");

const copyButton =
    document.getElementById("copyButton");


let currentTask = "qa";


const taskConfig = {

    qa: {
        label: "Your question",
        placeholder:
            "Example: What is machine learning?",
        button:
            "Ask EduGenie",
        title:
            "Question & Answer"
    },

    explain: {
        label: "Topic to explain",
        placeholder:
            "Example: Explain object-oriented programming.",
        button:
            "Explain Concept",
        title:
            "Concept Explanation"
    },

    quiz: {
        label: "Educational text",
        placeholder:
            "Paste a paragraph or lesson here to generate a quiz.",
        button:
            "Generate Quiz",
        title:
            "Your Quiz"
    },

    summarize: {
        label: "Text to summarize",
        placeholder:
            "Paste the educational passage you want to summarize.",
        button:
            "Summarize",
        title:
            "Summary"
    },

    learning: {
        label: "Topic you want to learn",
        placeholder:
            "Example: Python programming for AI and ML.",
        button:
            "Build Learning Path",
        title:
            "Personalized Learning Path"
    }

};


taskButtons.forEach(button => {

    button.addEventListener("click", () => {

        taskButtons.forEach(item => {
            item.classList.remove("active");
        });

        button.classList.add("active");

        currentTask =
            button.dataset.task;

        updateTaskUI();

        clearResult();
    });

});


function updateTaskUI() {

    const config =
        taskConfig[currentTask];

    inputLabel.textContent =
        config.label;

    userInput.placeholder =
        config.placeholder;

    submitText.textContent =
        config.button;

    if (currentTask === "learning") {

        levelContainer.classList.remove(
            "hidden"
        );

    } else {

        levelContainer.classList.add(
            "hidden"
        );

    }

}


userInput.addEventListener(
    "input",
    () => {

        characterCount.textContent =
            userInput.value.length;

    }
);


form.addEventListener(
    "submit",
    async event => {

        event.preventDefault();

        const input =
            userInput.value.trim();

        if (!input) {

            showError(
                "Please enter some content first."
            );

            return;
        }

        setLoading(true);

        try {

            let endpoint;
            let body;

            if (currentTask === "qa") {

                endpoint = "/qa";

                body = {
                    text: input
                };

            }

            else if (currentTask === "explain") {

                endpoint = "/explain";

                body = {
                    topic: input
                };

            }

            else if (currentTask === "quiz") {

                endpoint = "/quiz";

                body = {
                    text: input
                };

            }

            else if (currentTask === "summarize") {

                endpoint = "/summarize";

                body = {
                    text: input
                };

            }

            else if (currentTask === "learning") {

                endpoint =
                    "/learn/recommendations";

                body = {
                    topic: input,
                    level: level.value
                };

            }


            const response =
                await fetch(
                    endpoint,
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body:
                            JSON.stringify(body)
                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    "Something went wrong."
                );

            }


            displayResult(data);

        }

        catch (error) {

            showError(
                error.message ||
                "Unable to process your request."
            );

        }

        finally {

            setLoading(false);

        }

    }
);


function displayResult(data) {

    resultSection.classList.remove(
        "hidden"
    );

    resultTitle.textContent =
        taskConfig[currentTask].title;


    resultContent.innerHTML = "";


    if (currentTask === "quiz") {

        renderQuiz(data.quiz);

        return;

    }


    const text =
        data.result || "No result returned.";

    const textElement =
        document.createElement("div");

    textElement.className =
        "result-text";

    textElement.textContent =
        text;

    resultContent.appendChild(
        textElement
    );

}


function renderQuiz(quiz) {

    if (!Array.isArray(quiz)) {

        showError(
            "Invalid quiz response."
        );

        return;

    }


    quiz.forEach(
        (item, index) => {

            const question =
                document.createElement(
                    "div"
                );

            question.className =
                "quiz-question";


            const heading =
                document.createElement(
                    "h3"
                );

            heading.textContent =
                `${index + 1}. ${item.question}`;


            question.appendChild(
                heading
            );


            const note =
                document.createElement(
                    "div"
                );

            note.className =
                "answer-note";


            item.options.forEach(
                option => {

                    const button =
                        document.createElement(
                            "button"
                        );

                    button.type =
                        "button";

                    button.className =
                        "quiz-option";

                    button.textContent =
                        option;


                    button.addEventListener(
                        "click",
                        () => {

                            const allOptions =
                                question.querySelectorAll(
                                    ".quiz-option"
                                );

                            allOptions.forEach(
                                optionButton => {

                                    optionButton.disabled =
                                        true;

                                }
                            );


                            if (
                                option ===
                                item.answer
                            ) {

                                button.classList.add(
                                    "correct"
                                );

                                note.textContent =
                                    "✓ Correct!";

                            }

                            else {

                                button.classList.add(
                                    "incorrect"
                                );

                                allOptions.forEach(
                                    optionButton => {

                                        if (
                                            optionButton
                                                .textContent ===
                                            item.answer
                                        ) {

                                            optionButton.classList.add(
                                                "correct"
                                            );

                                        }

                                    }
                                );

                                note.textContent =
                                    `✗ Incorrect. Correct answer: ${item.answer}`;

                            }

                        }
                    );


                    question.appendChild(
                        button
                    );

                }
            );


            question.appendChild(
                note
            );


            resultContent.appendChild(
                question
            );

        }
    );

}


function showError(message) {

    resultSection.classList.remove(
        "hidden"
    );

    resultTitle.textContent =
        "Something went wrong";

    resultContent.innerHTML = "";


    const error =
        document.createElement(
            "div"
        );

    error.className =
        "result-text";

    error.textContent =
        message;

    resultContent.appendChild(
        error
    );

}


function clearResult() {

    resultSection.classList.add(
        "hidden"
    );

    resultContent.innerHTML =
        "";

}


function setLoading(isLoading) {

    submitButton.disabled =
        isLoading;

    loadingSpinner.classList.toggle(
        "hidden",
        !isLoading
    );


    if (isLoading) {

        submitText.textContent =
            "EduGenie is thinking...";

    }

    else {

        submitText.textContent =
            taskConfig[currentTask].button;

    }

}


copyButton.addEventListener(
    "click",
    async () => {

        const text =
            resultContent.innerText;

        if (!text) {
            return;
        }

        try {

            await navigator.clipboard.writeText(
                text
            );

            copyButton.textContent =
                "Copied!";

            setTimeout(
                () => {
                    copyButton.textContent =
                        "Copy";
                },
                1500
            );

        }

        catch {

            copyButton.textContent =
                "Copy failed";

        }

    }
);


updateTaskUI();