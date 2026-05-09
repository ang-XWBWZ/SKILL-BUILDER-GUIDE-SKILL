# Call-Chain Tracing Patterns by Architecture

## Layered Backend (NestJS, Spring, Django)

```
Controller.handler(req: RequestDto)
  → Service.process(dto: RequestDto)
    → Repository.find(where: QueryConditions)
      → Database.query(SQL)
    → ExternalClient.call(payload: ApiContract)
  → ResponseDto.from(entity)
```

Key checks: param validation at controller, transaction boundaries at service, query parameter types at repository.

## CLI Tool (Cobra, Click)

```
main() → rootCmd.Execute()
  → {command}.RunE(cmd, args)
    → {service}.Validate(args) → error
    → {service}.Execute(validated Input)
      → {output}.Format(result) → stdout
```

Key checks: flag types match service params, error types consistent across layers, output always goes to correct writer.

## Event-Driven / Message Queue

```
Consumer.Handle(message: RawMessage)
  → Deserialize(message) → EventDto
  → Processor.Process(event: EventDto)
    → Repository.Update(id, newState)
    → Publisher.Publish(ResultEvent)
```

Key checks: message schema matches between producer and consumer, idempotency handling, DLQ configuration.

## Frontend (React, Vue)

```
UserAction → EventHandler(action)
  → StateManager.dispatch(action: ActionType, payload)
    → APIClient.request(method, url, body) → Promise<Response>
  → StateManager.commit(mutation, response.data)
  → Component.render(updatedState)
```

Key checks: action types match between component and store, API response types match state types, error state handled in all components.

## Customization for Project-Specific Skills

1. Map the project's actual layer names to the tracing template (don't force Standard → Controller)
2. Add the project's external API call signatures to the type-matching checklist
3. Include project-specific error handling patterns (e.g. Result<T, E> in Rust, Either in FP)
4. Verify one real endpoint's full chain as a worked example in the generated skill
