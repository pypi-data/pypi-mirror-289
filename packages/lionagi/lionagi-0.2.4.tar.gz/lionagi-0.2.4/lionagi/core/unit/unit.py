"""
Copyright 2024 HaiyangLi

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from lionagi.libs.ln_convert import strip_lower
from lionagi.libs.ln_func_call import rcall
from lionagi.core.collections.abc import Directive
from lionagi.core.validator.validator import Validator
from lionagi.core.collections import iModel
from .unit_form import UnitForm
from .unit_mixin import DirectiveMixin
from .util import retry_kwargs


class Unit(Directive, DirectiveMixin):
    """
    Unit is a class that extends Directive and DirectiveMixin to provide
    advanced operations like chat, direct actions, and predictions using a
    specific branch and model.

    Attributes:
        branch (Branch): The branch instance associated with the Unit.
        imodel (iModel): The model instance used for the Unit.
        form_template (Type[Form]): The form template to use for operations.
        validator (Validator): The validator instance for response validation.
    """

    default_template = UnitForm

    def __init__(
        self, branch, imodel: iModel = None, template=None, rulebook=None, verbose=False
    ) -> None:
        self.branch = branch
        if imodel and isinstance(imodel, iModel):
            branch.imodel = imodel
            self.imodel = imodel
        else:
            self.imodel = branch.imodel
        self.form_template = template or self.default_template
        self.validator = Validator(rulebook=rulebook) if rulebook else Validator()
        self.verbose = verbose

    async def chat(
        self,
        instruction=None,
        context=None,
        system=None,
        sender=None,
        recipient=None,
        branch=None,
        requested_fields=None,
        form=None,
        tools=False,
        invoke_tool=True,
        return_form=True,
        strict=False,
        rulebook=None,
        imodel=None,
        clear_messages=False,
        use_annotation=True,
        return_branch=False,
        **kwargs,
    ):
        """
        Asynchronously performs a chat operation.

        Args:
            instruction (str, optional): Instruction message.
            context (str, optional): Context message.
            system (str, optional): System message.
            sender (str, optional): Sender identifier.
            recipient (str, optional): Recipient identifier.
            branch (Branch, optional): Branch instance.
            requested_fields (list, optional): Fields requested in the response.
            form (Form, optional): Form data.
            tools (bool, optional): Flag indicating if tools should be used.
            invoke_tool (bool, optional): Flag indicating if tools should be invoked.
            return_form (bool, optional): Flag indicating if form should be returned.
            strict (bool, optional): Flag indicating if strict validation should be applied.
            rulebook (Rulebook, optional): Rulebook instance for validation.
            imodel (iModel, optional): Model instance.
            clear_messages (bool, optional): Flag indicating if messages should be cleared.
            use_annotation (bool, optional): Flag indicating if annotations should be used.
            return_branch (bool, optional): Flag indicating if branch should be returned.
            kwargs: Additional keyword arguments.

        Returns:
            Any: The processed response.
        """
        kwargs = {**retry_kwargs, **kwargs}
        return await rcall(
            self._chat,
            instruction=instruction,
            context=context,
            system=system,
            sender=sender,
            recipient=recipient,
            branch=branch,
            requested_fields=requested_fields,
            form=form,
            tools=tools,
            invoke_tool=invoke_tool,
            return_form=return_form,
            strict=strict,
            rulebook=rulebook,
            imodel=imodel,
            clear_messages=clear_messages,
            use_annotation=use_annotation,
            return_branch=return_branch,
            **kwargs,
        )

    async def direct(
        self,
        instruction=None,
        *,
        context=None,
        form=None,
        branch=None,
        tools=None,
        return_branch=False,
        reason: bool = False,
        predict: bool = False,
        score=None,
        select=None,
        plan=None,
        allow_action: bool = False,
        allow_extension: bool = False,
        max_extension: int = None,
        confidence=None,
        score_num_digits=None,
        score_range=None,
        select_choices=None,
        plan_num_step=None,
        predict_num_sentences=None,
        directive: str = None,
        verbose=None,
        **kwargs,
    ):
        """
        Asynchronously directs the operation based on the provided parameters.

        Args:
            instruction (str, optional): Instruction message.
            context (str, optional): Context message.
            form (Form, optional): Form data.
            branch (Branch, optional): Branch instance.
            tools (Any, optional): Tools to be used.
            return_branch (bool, optional): Flag indicating if branch should be returned.
            reason (bool, optional): Flag indicating if reason should be included.
            predict (bool, optional): Flag indicating if prediction should be included.
            score (Any, optional): Score parameters.
            select (Any, optional): Select parameters.
            plan (Any, optional): Plan parameters.
            allow_action (bool, optional): Flag indicating if action should be allowed.
            allow_extension (bool, optional): Flag indicating if extension should be allowed.
            max_extension (int, optional): Maximum extension value.
            confidence (Any, optional): Confidence parameters.
            score_num_digits (int, optional): Number of digits for score.
            score_range (tuple, optional): Range for score.
            select_choices (list, optional): Choices for selection.
            plan_num_step (int, optional): Number of steps for plan.
            predict_num_sentences (int, optional): Number of sentences for prediction.
            directive (str, optional): Directive for the operation.
            kwargs: Additional keyword arguments.

        Returns:
            Any: The processed response.
        """
        kwargs = {**retry_kwargs, **kwargs}
        verbose = verbose if verbose is not None else self.verbose

        if not directive:

            out = await rcall(
                self._direct,
                instruction=instruction,
                context=context,
                form=form,
                branch=branch,
                tools=tools,
                return_branch=return_branch,
                reason=reason,
                predict=predict,
                score=score,
                select=select,
                plan=plan,
                allow_action=allow_action,
                allow_extension=allow_extension,
                max_extension=max_extension,
                confidence=confidence,
                score_num_digits=score_num_digits,
                score_range=score_range,
                select_choices=select_choices,
                plan_num_step=plan_num_step,
                predict_num_sentences=predict_num_sentences,
                verbose=verbose,
                **kwargs,
            )

            if verbose:
                print(
                    "\n--------------------------------------------------------------"
                )
                print(f"Directive successfully completed!")

            return out

        out = await rcall(
            self._mono_direct,
            directive=directive,
            instruction=instruction,
            context=context,
            branch=branch,
            tools=tools,
            verbose=verbose,
            **kwargs,
        )

        if verbose:
            print("--------------------------------------------------------------")
            print(f"Directive successfully completed!")

        return out

    async def select(self, *args, **kwargs):
        """
        Asynchronously performs a select operation using the _select method with
        retry logic.

        Args:
            *args: Positional arguments to pass to the _select method.
            **kwargs: Keyword arguments to pass to the _select method, including
                retry configurations.

        Returns:
            Any: The result of the select operation.
        """
        from .template.select import SelectTemplate

        kwargs = {**retry_kwargs, **kwargs}
        kwargs["template"] = kwargs.get("template", SelectTemplate)
        return await rcall(self._select, *args, **kwargs)

    async def predict(self, *args, **kwargs):
        """
        Asynchronously performs a predict operation using the _predict method with
        retry logic.

        Args:
            *args: Positional arguments to pass to the _predict method.
            **kwargs: Keyword arguments to pass to the _predict method, including
                retry configurations.

        Returns:
            Any: The result of the predict operation.
        """
        from .template.predict import PredictTemplate

        kwargs = {**retry_kwargs, **kwargs}
        kwargs["template"] = kwargs.get("template", PredictTemplate)
        return await rcall(self._predict, *args, **kwargs)

    async def score(self, *args, **kwargs):
        """
        Asynchronously performs a score operation using the _score method with retry logic.

        Args:
            *args: Positional arguments to pass to the _score method.
            **kwargs: Keyword arguments to pass to the _score method, including retry configurations.

        Returns:
            Any: The result of the score operation.
        """
        from .template.score import ScoreTemplate

        kwargs = {**retry_kwargs, **kwargs}
        kwargs["template"] = kwargs.get("template", ScoreTemplate)
        return await rcall(self._score, *args, **kwargs)

    async def plan(self, *args, **kwargs):
        """
        Asynchronously performs a plan operation using the _plan method with retry logic.

        Args:
            *args: Positional arguments to pass to the _plan method.
            **kwargs: Keyword arguments to pass to the _plan method, including retry configurations.

        Returns:
            Any: The result of the plan operation.
        """
        from .template.plan import PlanTemplate

        kwargs = {**retry_kwargs, **kwargs}
        kwargs["template"] = kwargs.get("template", PlanTemplate)
        return await rcall(self._plan, *args, **kwargs)

    async def _mono_direct(
        self,
        directive: str,  # examples, "chat", "predict", "act"
        instruction=None,  # additional instruction
        context=None,  # context to perform the instruction on
        system=None,  # optionally swap system message
        branch=None,
        tools=None,
        template=None,
        verbose=None,
        **kwargs,
    ):
        """
        Asynchronously performs a single direct operation.

        Args:
            directive (str): The directive for the operation.
            instruction (str, optional): Additional instruction.
            context (str, optional): Context for the operation.
            system (str, optional): System message.
            branch (Branch, optional): Branch instance.
            tools (Any, optional): Tools to be used.
            template (Any, optional): Template for the operation.
            kwargs: Additional keyword arguments.

        Returns:
            Any: The result of the direct operation.
        """

        if template:
            kwargs["template"] = template

        kwargs = {**retry_kwargs, **kwargs}
        branch = branch or self.branch

        if system:
            branch.add_message(system=system)

        if hasattr(self, strip_lower(directive)):
            directive = getattr(self, strip_lower(directive))

            verbose = verbose if verbose is not None else self.verbose
            if verbose:
                print(f"Performing directive: {directive}...")

            return await directive(
                context=context,
                instruction=instruction,
                tools=tools,
                **kwargs,
            )

        raise ValueError(f"invalid directive: {directive}")
