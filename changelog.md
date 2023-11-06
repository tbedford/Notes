# Quix Changelog

### 2.0.1 | 3 November 2023

## New features, performance improvements and bug squashing

`NEW FEATURES`

* New Replay service feature! Users can replay any persisted stream to a Topic as if it was happening now. This feature has been added on Persisted Streams, Pipeline view and Deployment details pages.

* Added new advanced configuration on Topics page. Users can now specify Retention and Partitions configuration when creating new Topics.

* Added new Run configuration on Projects IDE. Users can now specify different environment variable values in each Run of the application without changing default values of the Environment variables.

* Added new Deployments list view on workspace home page.

* Added new External Destination item to the library to signal when a pipeline is sending data to an external system.

* Allow users to save code as a project from the Library, even if they haven't completed the library item setup and configuration.

`IMPROVEMENT`

* Several performance improvements across the platform.

* Added AWS support. Platform is now compatible with Elastic Kubernetes Service (AKS) installation.

* Added (*) star functionality to the Streaming Reader service. Users can now subscribe to all the Streams, all the Parameters or all the Events of a Topic.

* Improved several error statuses on Topics page.

* Several improvements in the Project IDE regarding file selection, tags and commits navigation.

`BUG FIXES`

* Fixed some refresh issues when changing Input/Output variables on Project IDE

* Fixed some visualization issues on Topic metrics component

* Fixed an issue in Data Explorer where null values were shown as 0 instead of null

* Fixed an issue in Data Explorer (Live view) where null values were not drawn properly in the waveform

* Fixed several empty states across the platform

* Fixed an issue in Persisted Streams when filtering by location

* Fixed some issues when selecting/unselecting Drafts on Pipeline view

* Fixed some issues on Data Explorer (Live view) when filtering for specific Stream / Parameters

* Fixed some issues working in Project IDE editor

* Fixed some issues when navigating to a specific branch from Deployments to the Project IDE

* Fixed an issue with the URL link of a deployment with public access

* Fixed an issue where you couldn't delete a User from the workspace

* Fixed some refresh issues on Pipeline view

* Fixed navigation issues on workspace Home

* Fixed some issues updating logs in real time from Project IDE


