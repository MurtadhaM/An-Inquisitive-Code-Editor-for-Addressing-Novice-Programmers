# An-Inquisitive-Code-Editor-for-Addressing-Novice-Programmers
---
### Abstract ![](https://img.shields.io/badge/Paper-Abstract-blue)

> Novice programmers often struggle to understand the behavior of their programs. This struggle is often due to misconceptions about how the program works. In this paper, we propose an inquisitive code editor that identifies, corrects, and prevents misconceptions of program behavior. Our editor identifies misconceptions by comparing the programmer's code to a database of known bugs and code smells. It corrects misconceptions by presenting interactive explanations of the program's behavior. Finally, it prevents misconceptions by generating test code and documentation to inform programmers of behavior changes. We believe that our editor will help novice programmers better understand their programs and improve their programming skills.

---
### Goals ![](https://img.shields.io/badge/Paper-Goals-red)

---
- **Identifying Misconceptions:**
  - Uses existing bug databases and code smell detectors.
  - Determines correct answers using program analysis techniques.
  - Aims for non-disruptive interaction with the editor.
  - Explores additional signals like programmer frustration.
  - Annotates problematic code instead of interrupting with dialog windows.

- **Correcting Misconceptions:**
  - Presents explanations based on specific misconceptions.
  - Explores interactive explanations, e.g., having programmers test specific inputs.
  - Aims for more engagement and better understanding compared to textual explanations.

- **Preventing Misconceptions:**
  - Utilizes three mechanisms: test code, targeted teaching, and aggregate feedback.
  - Generates test code and documentation to inform programmers of behavior changes.
  - Monitors programmer struggles to teach specific topics.
  - Provides aggregate feedback to instructors on student misconceptions.

---

### Implementation ![](https://img.shields.io/badge/Paper-Implementation-green)
- Uses pre-existing tools for bug detection and program analysis.
- Jupyter notebooks for interactive explanations.
- Uses a web-based editor for non-disruptive interaction.
---
### Authors ![](https://img.shields.io/badge/Paper-Authors-yellow)

<table>
  <thead>
    <tr>
      <th>Murtadha Marzouq</th>
      <th align="center">Ryan Hull</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <a href="/MurtadhaM/VISUALIZATION/blob/main">
          <img src="https://camo.githubusercontent.com/9079488b3f7415f5bfc8d802fd945b73ee6bf29c0da2b9e90e543fa0c8c23cd1/68747470733a2f2f63617073746f6e652d66726f6e742d656e642d6c696d652e76657263656c2e6170702f5f6e6578742f696d6167653f75726c3d2532465465616d50686f746f732532464d757274616468615f4d61727a6f75712e706e6726773d33383426713d3735" alt="Murtadha Marzouq" data-canonical-src="https://capstone-front-end-lime.vercel.app/_next/image?url=%2FTeamPhotos%2FMurtadha_Marzouq.png&amp;w=384&amp;q=75" style="max-width: 100%;">
        </a>
      </td>
      <td>
        <a href="/MurtadhaM/VISUALIZATION/blob/main">
          <img src="https://camo.githubusercontent.com/60137fa7ff9ce9e838825d980d6a154a3eac47e4fa48b52a3c90202b51c1e07b/68747470733a2f2f63617073746f6e652d66726f6e742d656e642d6c696d652e76657263656c2e6170702f5f6e6578742f696d6167653f75726c3d2532465465616d50686f746f732532465279616e5f48756c6c2e6a70656726773d33383426713d3735" alt="Ryan Hull" data-canonical-src="https://capstone-front-end-lime.vercel.app/_next/image?url=%2FTeamPhotos%2FRyan_Hull.jpeg&amp;w=384&amp;q=75" style="max-width: 100%;">
        </a>
      </td>
    </tr>
  </tbody>
</table>

---

### Citation ![](https://img.shields.io/badge/Paper-Citation-orange)


```latex
@INPROCEEDINGS{9402182,
  author={Henley, Austin and Ball, Julian and Klein, Benjamin and Rutter, Aiden and Lee, Dylan},
  booktitle={2021 IEEE/ACM 43rd International Conference on Software Engineering: Software Engineering Education and Training (ICSE-SEET)}, 
  title={An Inquisitive Code Editor for Addressing Novice Programmers' Misconceptions of Program Behavior}, 
  year={2021},
  volume={},
  number={},
  pages={165-170},
  doi={10.1109/ICSE-SEET52601.2021.00026}}

  @INPROCEEDINGS{4814141,
  author={Ko, Andrew and Myers, Brad},
  booktitle={2008 ACM/IEEE 30th International Conference on Software Engineering}, 
  title={Debugging reinvented}, 
  year={2008},
  volume={},
  number={},
  pages={301-310},
  doi={10.1145/1368088.1368130}}
```