package ftn.backendservice.exception;

import ftn.backendservice.exception.exceptions.AuthorizationException;
import ftn.backendservice.exception.exceptions.BadRequestException;
import ftn.backendservice.exception.exceptions.ForbiddenException;
import ftn.backendservice.exception.exceptions.NotFoundException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;


@ControllerAdvice
@Slf4j
public class ControllerExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<?> handleValidation(MethodArgumentNotValidException exception) {
        log.error(exception.getMessage(), exception);
        String errorMessage = exception.getBindingResult().getAllErrors().get(0).getDefaultMessage();
        return ResponseEntity.status(400).body(new ExceptionMessage("Invalid form: " + errorMessage));
    }

    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<?> handleNotFound(NotFoundException exception) {
        log.error(exception.getMessage(), exception);
        HttpStatus status = getResponseStatus(exception.getClass());
        return ResponseEntity.status(status).body(new ExceptionMessage(exception.getMessage()));
    }

    @ExceptionHandler(ForbiddenException.class)
    public ResponseEntity<?> handleForbidden(ForbiddenException exception) {
        log.error(exception.getMessage(), exception);
        HttpStatus status = getResponseStatus(exception.getClass());
        return ResponseEntity.status(status).body(new ExceptionMessage("Forbidden: " + exception.getMessage()));
    }

    @ExceptionHandler(BadRequestException.class)
    public ResponseEntity<?> handleBadRequest(BadRequestException exception) {
        log.error(exception.getMessage(), exception);
        HttpStatus status = getResponseStatus(exception.getClass());
        return ResponseEntity.status(status).body(new ExceptionMessage(exception.getMessage()));
    }

    @ExceptionHandler(AuthorizationException.class)
    public ResponseEntity<?> handleAuthorization(AuthorizationException exception) {
        log.error(exception.getMessage(), exception);
        HttpStatus status = getResponseStatus(exception.getClass());
        return ResponseEntity.status(status).body(new ExceptionMessage(exception.getMessage()));
    }

    private HttpStatus getResponseStatus(Class<? extends Throwable> exceptionClass) {
        ResponseStatus responseStatus = exceptionClass.getAnnotation(ResponseStatus.class);
        if (responseStatus != null) {
            return responseStatus.value();
        }
        return HttpStatus.INTERNAL_SERVER_ERROR;
    }

}
