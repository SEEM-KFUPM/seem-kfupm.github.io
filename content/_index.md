---
title: 'SEEM — KFUPM'
type: landing
sections:
  - block: hero
    content:
      announcement:
        text: "Prototype website — content under review"
      title: "Smart Earth Exploration & Monitoring"
      text: "SEEM is a research group at the College of Petroleum Engineering & Geosciences, King Fahd University of Petroleum and Minerals. We develop data-driven methods for observing, understanding, and imaging the subsurface."
      primary_action:
        text: Explore our research
        url: /research/
      secondary_action:
        text: View selected software
        url: /projects/
    design:
      spacing:
        padding: ['6rem', 0, '6rem', 0]
  - block: research-areas
    content:
      title: Research at SEEM
      subtitle: From sensing to interpretable subsurface insight
      text: "We connect geoscience, signal processing, and machine learning to make complex Earth data more useful."
      items:
        - name: Seismic monitoring & localization
          description: "Methods for detecting and locating microseismic events from seismic and distributed sensing data."
          icon: hero/signal
          gradient: from-cyan-700 to-blue-900
          status: active
          topics: [Microseismicity, Event detection, Localization]
          cta:
            text: Explore research
            url: /research/
        - name: Distributed acoustic sensing
          description: "Learning-based workflows for denoising and extracting insight from DAS and VSP observations."
          icon: hero/adjustments-horizontal
          gradient: from-emerald-700 to-teal-900
          status: active
          topics: [DAS, Denoising, VSP]
          cta:
            text: Explore research
            url: /research/
        - name: Neural operators & reconstruction
          description: "Physics-informed and Fourier neural operators for robust reconstruction and inversion of seismic data."
          icon: hero/cpu-chip
          gradient: from-slate-700 to-indigo-950
          status: active
          topics: [Neural operators, Reconstruction, Inversion]
          cta:
            text: View project
            url: /projects/seisreconno/
        - name: Explainable AI & interpretation
          description: "Transparent machine-learning approaches for geophysical interpretation and geological reconstruction."
          icon: hero/magnifying-glass
          gradient: from-amber-700 to-orange-900
          status: emerging
          topics: [Explainable AI, Interpretation, Geology]
          cta:
            text: Explore research
            url: /research/
    design:
      layout: cards
  - block: collection
    content:
      title: Selected project & software
      subtitle: Curated research outputs with their technical evidence on GitHub.
      count: 3
      filters:
        folders: [projects]
        featured_only: true
      cta:
        text: All projects & software
        url: /projects/
    design:
      view: card
      columns: 3
  - block: collection
    content:
      title: Selected publication
      subtitle: A BibTeX-backed example of the site’s publication workflow.
      count: 3
      filters:
        folders: [publications]
        featured_only: true
      cta:
        text: All publications
        url: /publications/
    design:
      view: citation
  - block: team-showcase
    content:
      title: People
      subtitle: A research group is made by its people.
      text: "This card demonstrates the future team-profile workflow. Public member details will be added after review."
      user_groups: [Prototype profile]
      sort_by: weight
      cta:
        text: Meet the team
        url: /people/
        icon: user-group
    design:
      show_role: true
      show_organizations: true
      show_interests: true
      max_interests: 3
      max_columns: 3
      show_social: true
  - block: collection
    content:
      title: Latest news
      subtitle: Small, reviewable updates will keep the group’s public record current.
      count: 3
      filters:
        folders: [blog]
      cta:
        text: All news
        url: /news/
    design:
      view: card
      columns: 3
  - block: contact-info
    content:
      title: Collaborate with SEEM
      subtitle: "We welcome research connections, feedback on our open-source work, and future opportunities to join the group."
      visit_title: Affiliation
      address:
        lines:
          - College of Petroleum Engineering & Geosciences
          - King Fahd University of Petroleum and Minerals
          - Dhahran, Saudi Arabia
      connect_title: Connect
      text: "Contact details and opportunities will be added after institutional review. Until then, explore the group’s public research software."
      social:
        - icon: brands/github
          label: SEEM-KFUPM on GitHub
          url: https://github.com/SEEM-KFUPM
---
