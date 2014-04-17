# [Agile Development](http://i.imgur.com/FcTiTuk.jpg)

Click on the title for a verbatim image from the meeting.

## "1. Defer building until pain"

This is also referred to as [kanban development](http://www.slideshare.net/JR0cket/jit-developmentwithkanbanjax-london2011).

This often happens with development:

* More urgent things come up
* There is always more to do
* There are hidden requirements
* Not enough time to finish your tasks

"Defer building until pain" means not building a feature until it is certain that a feature will be used. For example:

* Making a fake button, implementing its underlying features only after many (see 6.) users have clicked on it

## "2. Deploy thin slices"

Instead of deploying a complete feature, deploy partial features. This will get a feature out to a customer as soon as possible, which helps detect bugs (see 6.) early.

The following are examples of deploying thin slices:

* Deploying individual bug fixes

### Deploy often

As slices become thinner and thinner, continuous deployment can be easily achieved. At that point, code reviews will need to be done as soon as possible, typically approved or rejected in under an hour.

## "3. Use 3rd party tools"

If someone somewhere has made a tool that does what we want to do, then that tool shall be used until the tool no longer does what we want to do (e.g. we want more features). 

Even so, if said tool is open source, we will want to either fork or contribute to the same tool to meet our increasing requirements. This should be the last resort (see 1.)

## "4. Architect Simply"

Put flexibility aside, because implementing flexibility vastly increases the complexity of the code, which conflicts with (4). 

Build exactly what is required of the task, and worry about the spaghetti code later.

## "5. Avoid task dependencies"

Don't wait for things to start working on your task. 

There are two types of dependencies that can prevent you from working: internal and external dependencies.

### "3rd party" (external)

If you need to wait on a third party (e.g. another company) for action to be taken on their side of business, such as adding an API or a script tag, in order for you to finish your task, simply...

### "March ahead" (internal)

Work as if all dependencies exist. 

If an API does not exist, pretend it does, and work on. 

If you depend on a feature that does not exist, pretend the feature exists, and work on.

## "6. Use data to make decisions"

Never guess what features people use, what people want or don't want, or which bugs are more important to fix. Leverage analytics tools available to you (see 3.) to find out:

* What increases software performance
* What features users use most often
* Which bugs are most often hit by users

## "7. Definition of Done"

In Kanban, there is a concept called "Plan - Do - Done", that divides all tasks into the three categories.

There are many occasions when you want to mark a task as done, but a task is only considered Done when the feature is deployed and tested.

If the feature turns out to be buggy, the task is still considered done. Just file another high priority task to fix that bug.